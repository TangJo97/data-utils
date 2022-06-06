import unittest

from main.rawdata import class_from_json


# python -m unittest -v utils/tests/rawdata/test_classfromjson.py
class TestClassFromJson(unittest.TestCase):
    def test_on_nested_json_data(self):
        data = {  # no need for key: dict because it should have been flatten already
            "id": 1,  # non optional
            "entryA": "valueA",
            "entryC": ["hello", "salut", "tanguy"],
            "entryD": [
                {
                    "entryE": [
                        {"entryF": 15, "entryG": "hello"},
                        {"entryF": 22, "entryG": "salut"},
                    ],
                    "entryH": 15,
                }
            ],
            "entryG": [],
            "entryF": [{"a": 10, "b": 20}],
            "entryP": [[["a", "b"], ["a", "b"]]],
            "entryB": None,
            "entryZ": {"a": 12, "b": 20},
        }
        class_name = "MyClass"

        result = f"""from typing import List, Optional
from pydantic import BaseModel


class {class_name}(BaseModel):
\tid: int
\tentryA: Optional[str]
\tentryC: List[str]
\tentryD: List[EntryD]
\tentryG: List[NoneType]
\tentryF: List[EntryF]
\tentryP: List[List[List[str]]]
\tentryB: Optional[NoneType]
\tentryZ: EntryZ


class EntryD(BaseModel):
\tentryE: List[EntryE]
\tentryH: Optional[int]


class EntryE(BaseModel):
\tentryF: Optional[int]
\tentryG: Optional[str]


class EntryF(BaseModel):
\ta: Optional[int]
\tb: Optional[int]


class EntryZ(BaseModel):
\ta: Optional[int]
\tb: Optional[int]"""
        self.maxDiff = None
        self.assertEqual(class_from_json(data, class_name), result)
