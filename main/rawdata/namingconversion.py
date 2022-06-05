# %%
from functools import reduce


def __capitalize_first_letter(word: str) -> str:
    return word[0].upper() + word[1:]


def __lower_first_letter(word: str) -> str:
    return word[0].lower() + word[1:]


def snake_case_to_camel_case(field: str, sep: str = "_") -> str:
    """
    Transform a snake case field into a camel case field

    - field: a snake case string
    - sep: The snake case separator, traditionnaly ```"_"```
    """
    b = field.split(sep)
    c = filter(lambda x: x, b)
    d = map(__capitalize_first_letter, c)
    return __lower_first_letter("".join(d))


def __maj_to_underscore_lower(agg: list[str], letter: str, sep: str) -> list[str]:
    agg += [sep, letter.lower()] if letter.isupper() else [letter]
    return agg


def camel_case_to_snake_case(field: str, sep: str = "_") -> str:
    """
    Transform a camel case string into a snake case field

    - field: a camel case string
    - sep: The snake case separator, traditionnaly ```"_"```
    """
    snake_case_letters = reduce(
        lambda agg, letter: __maj_to_underscore_lower(agg, letter, sep),
        field[1:],
        [field[0].lower()],
    )
    return "".join(snake_case_letters)


def to_pascal_case(field: str, sep="__") -> str:
    """
    Transform any string into PascalCase

    - field: a string
    - sep: string or character that separate the different words (e.g. if snake
    case string, it would be ```"_"```)
    """
    elements = field.split(sep)
    if len(elements) == 0:
        only_element = elements[0]
        return only_element[0].upper() + b[1:]
    capitalized_elements = map(__capitalize_first_letter, elements)
    return "".join(capitalized_elements)


# FIXME: maybe add this
# def to_pascal_case_keep_sep(field: str, sep="__") -> str:
#     elements = field.split(sep)
#     if len(elements) == 0:
#         only_element = elements[0]
#         return only_element[0].upper() + b[1:]
#     capitalized_elements = map(__capitalize_first_letter, elements)
#     return sep.join(capitalized_elements)
