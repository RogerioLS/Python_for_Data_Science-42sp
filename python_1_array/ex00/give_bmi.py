import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Calculates the BMI (Body Mass Index) for a list of heights and weights.

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[int | float]: A list of calculated BMI values.

    Raises:
        TypeError: If inputs are not lists of ints/floats.
        ValueError: If list dimensions are not equal or contain negative/zero values.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Inputs must be lists.")

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same size.")

    for h, w in zip(height, weight):
        # In Python, bool is a subclass of int (isinstance(True, int) is True).
        # We must explicitly filter out bool to ensure strict type checking.
        if type(h) not in (int, float) or type(w) not in (int, float):
            raise TypeError("List elements must be integers or floats.")
        if h <= 0 or w <= 0:
            raise ValueError("Height and weight must be greater than zero.")

    h_arr = np.array(height, dtype=float)
    w_arr = np.array(weight, dtype=float)

    bmi_arr = w_arr / (h_arr ** 2)
    return bmi_arr.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Checks if BMI values in a list exceed a given limit.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The BMI threshold limit.

    Returns:
        list[bool]: A list of booleans, True if the BMI exceeds the limit.

    Raises:
        TypeError: If bmi is not a list of ints/floats, or limit is not an int/float.
    """
    if not isinstance(bmi, list):
        raise TypeError("BMI input must be a list.")
    if type(limit) not in (int, float):
        raise TypeError("Limit must be an integer or float.")

    for b in bmi:
        if type(b) not in (int, float):
            raise TypeError("BMI elements must be integers or floats.")

    bmi_arr = np.array(bmi, dtype=float)
    return (bmi_arr > limit).tolist()
