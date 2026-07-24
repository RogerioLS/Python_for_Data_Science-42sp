"""Tester script for ex05 (Pimp my image)."""

from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import numpy as np


def main() -> None:
    """Load landscape.jpg, apply filters, and print invert docstring."""
    try:
        array = ft_load("landscape.jpg")
        if array is None:
            raise ValueError("Failed to load image array.")

        # Apply filters (which will also display the images)
        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)

        # Print the docstring of ft_invert as required by the subject
        print(ft_invert.__doc__)
    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()
