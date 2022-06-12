# %%
import argparse
import json
from functools import reduce
from typing import Any, Dict, List

from .israwstructures import isiterable, isvector
from .namingconversion import to_pascal_case


# %%
def __dico_to_class_fields_wrapper(original_dico: dict, class_name: str):
    list_of_classes = []

    def __dico_to_class_fields(original_dico: dict, class_name: str):
        class_dico = {"class": class_name}
        list_of_classes.append(class_dico)
        for key, value in original_dico.items():
            if not isiterable(value):
                class_dico[key] = (
                    f"Optional[{type(value).__name__}]"
                    if key != "id"
                    else type(value).__name__
                )
            elif isinstance(value, dict):
                class_dico[key] = to_pascal_case(key)
                list_of_classes.append(
                    __dico_to_class_fields(value, to_pascal_case(key))
                )
            elif isvector(value):
                class_dico[key] = (
                    "List" + f"[{__get_inner_type_vector(value, to_pascal_case(key))}]"
                )

    def __get_inner_type_vector(original_vector: "set | list | tuple", key) -> str:
        original_vector_list = list(original_vector)
        if original_vector_list:
            first_value = original_vector_list[
                0
            ]  # assume same structure everywhere in the list
            if not isiterable(first_value):
                return type(first_value).__name__
            elif isvector(first_value):
                return "List" + f"[{__get_inner_type_vector(first_value, key)}]"
            elif isinstance(first_value, dict):
                list_of_classes.append(
                    __dico_to_class_fields(first_value, class_name=key)
                )
                return to_pascal_case(key)
        else:
            return "NoneType"

    __dico_to_class_fields(original_dico, class_name)
    return list_of_classes


def __dico_fields_to_case_class_string(one_class):
    class_name = list(filter(lambda x: x[0] == "class", one_class.items()))[0][1]
    fields = filter(lambda x: x[0] != "class", one_class.items())
    class_name_field = f"class {class_name}(BaseModel):"
    return (
        class_name_field
        + "\n\t"
        + "\n\t".join(list(map(lambda x: f"{x[0]}: {x[1]}", fields)))
    )


def reduce_json_to_one_example(data) -> Dict[Any, Any]:
    if isvector(data):
        return __reduce_json(data)
    else:
        return data


def __json_take_most_filled(
    accumulator: Dict[Any, Any], inner_json_data: Dict[Any, Any]
) -> Dict[Any, Any]:
    count_nb_filled_fields = lambda x, y: x + 1 if y[1] else 0
    count_filled = reduce(
        count_nb_filled_fields, inner_json_data.items(), 0
    )  # if non-empty
    count_filled_accumulator = reduce(count_nb_filled_fields, accumulator.items(), 0)
    return inner_json_data if count_filled > count_filled_accumulator else accumulator


def __reduce_json(json_data: List[Dict[Any, Any]]) -> Dict[Any, Any]:
    # return json_data[0]
    return reduce(__json_take_most_filled, json_data)


def class_from_json(json_example, class_name):
    """
    Auto generate case classes (in string format, which can be dumped into a .py file)
    from example JSON data.

    - json_example: Should be JSON serializable
    - class_name: The name of the main class
    """
    imports = "\n".join(
        ["from typing import List, Optional", "from pydantic import BaseModel"]
    )
    list_of_classes = __dico_to_class_fields_wrapper(json_example, class_name)
    list_of_classes_without_Nones = filter(lambda x: x is not None, list_of_classes)
    list_string_classes = map(
        __dico_fields_to_case_class_string, list_of_classes_without_Nones
    )
    joined_classes = ("\n" * 3).join(list_string_classes)
    return imports + "\n" * 3 + joined_classes


# argpase, Impure
def classfromjson():
    my_parser = argparse.ArgumentParser(
        description="Create case classes from an example JSON data",
        epilog="Be careful that it can overwrite existing files!",
    )
    my_parser.add_argument(
        "PathJsonExample",
        metavar="path_example",
        type=str,
        help="the path to the json examples",
    )
    my_parser.add_argument(
        "outputPath",
        metavar="output_path",
        type=str,
        help="The path of the .py file to generate",
    )

    my_parser.add_argument(
        "-c",
        "--className",
        metavar="class_name",
        type=str,
        help="The name of the main class to generate",
        default="Main",
    )
    args = my_parser.parse_args()
    input_path = args.PathJsonExample
    with open(input_path, "r") as f:
        data = json.load(f)
    json_example = reduce_json_to_one_example(data)
    print(f"Getting JSON example from {input_path}")

    generated_classes_str = class_from_json(json_example, args.className)
    with open(args.outputPath, "w") as out_f:
        out_f.write(generated_classes_str)
    print(f"Outputted the generated classes to {args.outputPath}")


if __name__ == "__main__":
    classfromjson()
