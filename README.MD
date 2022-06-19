# Introduction
## Table of Content
- [Introduction](#introduction)
  - [Table of Content](#table-of-content)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Generate data model from JSON data](#generate-data-model-from-json-data)
    - [Flatten JSON data](#flatten-json-data)
  - [License](#license)

This project will help you deal with data operations.
Notably, it will:

1. Auto-generate `Pydantic` models from example JSON data
1. Flatten nested JSON data
1. Convert Snake case string to camel case string & vice-versa 

## Installation

You can clone this repository locally & use pip to install it.

```bash
pip install <path-to-this-folder>
```

## Usage

### Generate data model from JSON data

Run the following:

```bash
classfromjson data.json models.py -c Main
```

where data.json:

```json
{
  "field1": [
    {
      "subfield1": 10,
      "subfield2": 20
    }
  ],
  "field2": "value2"
}
```

The result would be inside `models.py`:

```python
from typing import List, Optional
from pydantic import BaseModel


class Main(BaseModel):
    field1: List[Field1]
    field2: Optional[str]

class Field1(BaseModel):
    subfield1: Optional[int]
    subfield2: Optional[int]
```

If `data.json` was a list of dictionnaries, it would select the least empty one.

If you want to convert your data to that schema, you simply need to:
```python
from json import load

with open("data.json") as f:
  data = load(f)

data_with_schema = Main.parse_obj(data) # if only one example
data_with_schema_list = map(lambda  x: Main.parse_obj(x), data) # if list of json
```

Note that if some values are empty, the type cannot be inferred. Therefore, the engine will default to put "NoneType". You can then replace it in the generated file. 
### Flatten JSON data

It can flatten any level of nesting in JSON data

```python
from rawdata import flatten_json

data = {
  "field1":
    {
      "subfield1": 10,
      "subfield2": 20
    }
  ,
  "field2": "value2"
}

flatten_json(data, sep = "_")
```

Would return:

```
{
  "field1_subfield1": 10,
  "field1_subfield2": 20,
  "field2": "value2"
}
```

It can of course go deeper in the nesting & can deal with list of dictionnaries by
flattening those nested dictionnaries

## License

[MIT](https://choosealicense.com/licenses/mit/)
