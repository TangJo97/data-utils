import unittest

from main.rawdata import (
    camel_case_to_snake_case,
    snake_case_to_camel_case,
    to_pascal_case,
)


# python -m unittest -v utils/tests/rawdata/test_namingconversion.py
class TestToPascalCase(unittest.TestCase):
    def test_on_snake_case_data(self):
        data = "tanguy_jooris_hello"
        result = "TanguyJoorisHello"
        self.assertEqual(to_pascal_case(data, sep="_"), result)

    def test_on_camel_case_data(self):
        data = "tanguyJoorisHello"
        result = "TanguyJoorisHello"
        self.assertEqual(to_pascal_case(data), result)

    def test_on_class_data(self):
        data = "TanguyJoorisHello"
        self.assertEqual(to_pascal_case(data), data)

    def test_on_flatten_data(self):
        data = "property__LivingRoom__size"
        result = "PropertyLivingRoomSize"
        self.assertEqual(to_pascal_case(data, sep="__"), result)


class TestSnakeCaseToCamelCase(unittest.TestCase):
    def test_on_snake_case_data(self):
        data = "tanguy_jooris_hello"
        result = "tanguyJoorisHello"
        self.assertEqual(snake_case_to_camel_case(data, sep="_"), result)

    def test_on_flatten_data(self):
        data = "property__LivingRoom__size"
        result = "propertyLivingRoomSize"
        self.assertEqual(snake_case_to_camel_case(data, sep="__"), result)


class TestCamelCaseToSnakeCase(unittest.TestCase):
    def test_on_camel_case_data(self):
        data = "tanguyJoorisHello"
        result = "tanguy_jooris_hello"
        self.assertEqual(camel_case_to_snake_case(data, sep="_"), result)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestToPascalCase))
    test_suite.addTest(unittest.makeSuite(TestSnakeCaseToCamelCase))
    test_suite.addTest(unittest.makeSuite(TestCamelCaseToSnakeCase))
    return test_suite


if __name__ == "__main__":
    mySuit = suite()
    runner = unittest.TextTestRunner()
    runner.run(mySuit)
