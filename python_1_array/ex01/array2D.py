"""Module for 2D array slicing and shape inspection.

This module provides the slice_me function, which slices a 2D array (list of lists)
along its first dimension, prints its shape before and after the slice,
and returns the sliced result.
"""

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slices a 2D list from start to end, prints original and new shape.

    Args:
        family (list): A 2D list containing sublists of the same size.
        start (int): Start index for slicing.
        end (int): End index for slicing.

    Returns:
        list: The sliced 2D list.

    Raises:
        TypeError: If family is not a list, or if start/end are not integers.
        ValueError: If family sublists do not have consistent sizes.
    """
    # Reject boolean explicitly since bool is a subclass of int
    if type(start) is not int or type(end) is not int:
        raise TypeError("start and end must be integers")

    if not isinstance(family, list):
        raise TypeError("family must be a list")

    # Validate that every element in family is a list (2D array requirement)
    for row in family:
        if not isinstance(row, list):
            raise TypeError("family must be a list of lists (2D list)")

    # Validate that all rows have the same size (unless empty)
    if len(family) > 0:
        first_row_len = len(family[0])
        for row in family:
            if len(row) != first_row_len:
                raise ValueError("All rows in the 2D array must have the same size")

    # Convert to numpy array to retrieve shape easily
    arr = np.array(family)
    print(f"My shape is : {arr.shape}")

    # Perform native Python slicing
    sliced_list = family[start:end]

    # Print new shape of the sliced list
    sliced_arr = np.array(sliced_list)
    print(f"My new shape is : {sliced_arr.shape}")

    return sliced_list
