def all_thing_is_obj(obj: any) -> int:
    """Prints the type of the given object and returns 42.

    Args:
        obj (any): Input object to analyze.

    Returns:
        int: Always returns 42.
    """
    obj_type = type(obj)

    if obj_type == list:
        print(f"List : {obj_type}")
    elif obj_type == tuple:
        print(f"Tuple : {obj_type}")
    elif obj_type == set:
        print(f"Set : {obj_type}")
    elif obj_type == dict:
        print(f"Dict : {obj_type}")
    elif obj_type == str:
        print(f"{obj} is in the kitchen : {obj_type}")
    else:
        print("Type not found")

    return 42