from main.rawdata import flatten_json
import unittest

# python -m unittest -v utils/tests/rawdata/test_flattenjson.py
class TestFlattenJson(unittest.TestCase):
    def test_multileveltesting(self):
        multilevelnesting = {
            "entry1_level1": [
                {"entry1": ["value1", "value2"]},
                {"entry2": ["value3", "value4"]},
            ],
            "entry2_level1": "value5",
            "entry3_level1": {"entry1_level2": [["entry"]]},
        }
        resultmultilevelnesting = {
            "entry1_level1": [
                {"entry1": ["value1", "value2"]},
                {"entry2": ["value3", "value4"]},
            ],
            "entry2_level1": "value5",
            "entry3_level1__entry1_level2": [["entry"]],
        }

        self.assertEqual(
            flatten_json(multilevelnesting, sep="__"), resultmultilevelnesting
        )

    def test_three_level_nesting(self):
        three_level_nesting = {"data": {"very": {"nested": 15}}}

        three_level_nesting_result = {"data;;;very;;;nested": 15}
        self.assertEqual(
            flatten_json(three_level_nesting, sep=";;;"), three_level_nesting_result
        )

    def test_list_with_nesting(self):
        list_with_nesting = {"data": [{"data1": {"data2": 15}}]}

        list_with_nesting_result = {"data": [{"data1__data2": 15}]}
        self.assertEqual(
            flatten_json(list_with_nesting, sep="__"), list_with_nesting_result
        )

    def test_with_nones(self):  # also test for the ' instead of "
        json_with_nones = {
            "property": {
                "building": {
                    "annexCount": None,
                    "condition": "TO_RENOVATE",
                    "constructionYear": 1968,
                    "facadeCount": 4,
                    "floorCount": 16,
                    "streetFacadeWidth": None,
                },
                "monthlyCosts": None,
                "type": "APARTMENT",
                "toiletCount": 1,
                "parkingCountIndoor": 1,
                "parkingCountClosedBox": None,
            }
        }

        json_with_nones_result = {
            "property__building__annexCount": None,
            "property__building__condition": "TO_RENOVATE",
            "property__building__constructionYear": 1968,
            "property__building__facadeCount": 4,
            "property__building__floorCount": 16,
            "property__building__streetFacadeWidth": None,
            "property__monthlyCosts": None,
            "property__type": "APARTMENT",
            "property__toiletCount": 1,
            "property__parkingCountIndoor": 1,
            "property__parkingCountClosedBox": None,
        }
        self.assertEqual(
            flatten_json(json_with_nones, sep="__"), json_with_nones_result
        )


if __name__ == "__main__":
    unittest.main()
