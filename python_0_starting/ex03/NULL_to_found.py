import math

def NULL_not_found(obj: any) -> int:
    """
    Check if the given object is a "NULL" value and print its type and name.

    The function checks for the following "NULL" values:
    - None: Represents the absence of a value.
    - NaN (Not a Number): Represents an undefined or unrepresentable value in floating-point calculations.
    - 0: Represents the integer zero.
    - "": Represents an empty string.
    - False: Represents the boolean value false.

    Args:
        obj (any): The object to be checked.
    
    Returns:
        int: 0 if the object is a "NULL" value, 1 otherwise.
    """
    obj_type = type(obj)

    if obj is None:
        print(f"Nothing: None {obj_type}")
    elif isinstance(obj, float) and math.isnan(obj):
        print(f"Cheese: nan {obj_type}")
    elif obj_type is int and obj == 0:
        print(f"Zero: {obj} {obj_type}")
    elif obj_type is str and obj == "":
        print(f"Empty: {obj_type}")
    elif obj_type is bool and obj is False:
        print(f"Fake: False {obj_type}")
    else:
        print("Type not Found")
        return 1
    return 0