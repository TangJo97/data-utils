import json
from collections.abc import Iterable


def isiterable(value) -> bool:
    """
    Tell whether the input is an iterable (string excluded)

    """
    return isinstance(value, Iterable) and not isinstance(value, str)


def isvector(value) -> bool:
    """
    Tell whether the input is a vector (an iterable excluding dictionnary)
    """
    return isiterable(value) and not isinstance(value, dict)


def isjson(x):
    """
    Tell whether this input is serializable in JSON format. Boolean result
    """
    try:
        json.dumps(x)
        return True
    except (TypeError, OverflowError):
        return False
