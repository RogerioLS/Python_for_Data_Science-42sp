"""Module containing functions to apply filters/effects to images using constrained operators."""

import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received using only =, +, -, * operators.

    Args:
        array (np.ndarray): The input RGB image array.

    Returns:
        np.ndarray: The inverted image array.
    """
    inverted = 255 - array
    plt.imshow(inverted)
    plt.title("Figure VIII.2: Invert")
    plt.show()
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red color channel of the image using only =, * operators.

    Args:
        array (np.ndarray): The input RGB image array.

    Returns:
        np.ndarray: The red filtered image array.
    """
    red_img = array.copy()
    red_img[:, :, 1] = red_img[:, :, 1] * 0
    red_img[:, :, 2] = red_img[:, :, 2] * 0
    plt.imshow(red_img)
    plt.title("Figure VIII.3: Red")
    plt.show()
    return red_img


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green color channel of the image using only =, - operators.

    Args:
        array (np.ndarray): The input RGB image array.

    Returns:
        np.ndarray: The green filtered image array.
    """
    green_img = array.copy()
    green_img[:, :, 0] = green_img[:, :, 0] - green_img[:, :, 0]
    green_img[:, :, 2] = green_img[:, :, 2] - green_img[:, :, 2]
    plt.imshow(green_img)
    plt.title("Figure VIII.4: Green")
    plt.show()
    return green_img


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue color channel of the image using only = operator.

    Args:
        array (np.ndarray): The input RGB image array.

    Returns:
        np.ndarray: The blue filtered image array.
    """
    blue_img = array.copy()
    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0
    plt.imshow(blue_img)
    plt.title("Figure VIII.5: Blue")
    plt.show()
    return blue_img


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale using only =, / operators.

    Args:
        array (np.ndarray): The input RGB image array.

    Returns:
        np.ndarray: The grayscale image array.
    """
    grey_img = array.copy()
    # np.sum is a function. The only operators used are / and =.
    grey_val = np.sum(array, axis=2) / 3
    grey_img[:, :, 0] = grey_val
    grey_img[:, :, 1] = grey_val
    grey_img[:, :, 2] = grey_val
    plt.imshow(grey_img.astype(np.uint8))
    plt.title("Figure VIII.6: Grey")
    plt.show()
    return grey_img
