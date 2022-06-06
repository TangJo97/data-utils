import unittest

from main.rawdata import isiterable, isjson, isvector


# python -m unittest -v utils/tests/rawdata/test_israwstructures.py
class TestIsJson(unittest.TestCase):
    def test_on_json_data(self):
        data = {
            "hello": "I am JSON",
            "count": [1, 2, 3, 4],
            "nested": {"first": {"second": [1, 2, 3]}},
        }
        self.assertTrue(isjson(data))

    def test_on_non_json_data(self):
        data = {
            "hello": isjson,
            "count": [1, 2, 3, 4],
            "nested": {"first": {"second": [1, 2, 3]}},
        }
        self.assertFalse(isjson(data))


class TestIsvector(unittest.TestCase):
    def test_on_vector_data(self):
        data = ["a", 5, isjson]
        self.assertTrue(isvector(data))

    def test_on_dict_data(self):
        data = {
            "hello": isvector,
            "count": [1, 2, 3, 4],
            "nested": {"first": {"second": [1, 2, 3]}},
        }
        self.assertFalse(isvector(data))

    def test_on_string(self):
        data = "hello"
        self.assertFalse(isvector(data))


class TestIsIterable(unittest.TestCase):
    def test_on_dict_data(self):
        data = {"hello": "adict", "size": 2}
        self.assertTrue(isiterable(data))

    def test_on_list_data(self):
        data = ["hello", 10, isjson]
        self.assertTrue(isiterable(data))

    def test_on_string(self):
        data = "jesuisstring"
        self.assertFalse(isiterable(data))


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestIsJson))
    test_suite.addTest(unittest.makeSuite(TestIsvector))
    test_suite.addTest(unittest.makeSuite(TestIsIterable))
    return test_suite


if __name__ == "__main__":
    mySuit = suite()
    runner = unittest.TextTestRunner()
    runner.run(mySuit)
