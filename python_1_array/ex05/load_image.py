"""Module to load images and convert them into NumPy arrays."""

import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray:
    """Loads an image from the specified path.

    Converts the image to RGB, prints its shape,
    and returns its pixel content as a NumPy array.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string.")
        # Load image using PIL
        with Image.open(path) as img:
            # Convert to RGB explicitly
            img_rgb = img.convert("RGB")
            # Convert to NumPy array
            img_array = np.array(img_rgb)
            # Print the shape of the image
            print(f"The shape of image is: {img_array.shape}")
            # Return the numpy array
            return img_array
    except FileNotFoundError:
        print(f"Error: The file at '{path}' was not found.")
    except UnidentifiedImageError:
        print(f"Error: The file at '{path}' is not a valid image or is corrupted.")
    except TypeError as te:
        print(f"Error: {te}")
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading the image: {e}")
    return None
