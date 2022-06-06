# %%
import json

from .israwstructures import isiterable, isvector


def __flatten_dico(original_dico: dict, sep: str, prefix="") -> dict:
    new_dico = dict()
    # assert that it is a Json or convert to it
    prefix_of_keys = prefix + sep if prefix else prefix
    for key, value in original_dico.items():
        if not isiterable(value):
            new_dico[prefix_of_keys + key] = value
        elif isinstance(value, dict):
            new_dico = {
                **new_dico,
                **__flatten_dico(value, sep=sep, prefix=prefix_of_keys + key),
            }
        elif isvector(value):
            new_dico[prefix_of_keys + key] = __flatten_vector(value, sep=sep)

    return new_dico


def __flatten_vector(
    original_vector: "set | list | tuple", sep: str
) -> "set | list | tuple":
    new_vector = []  # c'est tjrs les mêmes cas
    for value in original_vector:
        if not isiterable(value):
            new_value = value
        elif isvector(value):
            new_value = __flatten_vector(value, sep)
        elif isinstance(value, dict):
            new_value = __flatten_dico(value, sep)

        new_vector.append(new_value)
    return new_vector


def flatten_json(json_data: "dict | list", sep: str = "__") -> "dict | list":
    """
    Flatten Json data. If you have a series of nested dictionnary, it will replace
    the nesting by a join of the nested keys.

    - json_data: Json data, Should support ```json.dumps``` on it
    - sep: the string or character that will separate the flatten keys
    """
    json.dumps(json_data)  # testing if it is serializable
    if not isiterable(json_data):
        new_value = json_data
    elif isvector(json_data):
        new_value = __flatten_vector(json_data, sep)
    elif isinstance(json_data, dict):
        new_value = __flatten_dico(json_data, sep)
    return new_value
