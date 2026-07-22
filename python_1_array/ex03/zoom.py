"""Module to load, slice (zoom), and display an image in grayscale."""

import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main() -> None:
    """Loads animal.jpeg, prints its shape and content, slices a 400x400 region

    with 1 color channel, prints the sliced shape and pixel content,
    and displays the zoomed grayscale image with scales on both axes.
    """
    try:
        # Load the image
        img = ft_load("animal.jpeg")
        if img is None:
            raise FileNotFoundError("Image 'animal.jpeg' could not be loaded.")

        # Print the loaded image array content
        print(img)

        # Slice the 400x400 region from the image with 1 color channel
        # The slice coordinates 100:500 (height) and 380:780 (width) target the raccoon
        sliced = img[100:500, 380:780, 0:1]

        # Print shape after slicing
        print(f"New shape after slicing: {sliced.shape} or {sliced.shape[:2]}")

        # Print the sliced array pixel content
        print(sliced)

        # Display the zoomed grayscale image using matplotlib
        # cmap="gray" is used to show it in grayscale.
        plt.imshow(sliced, cmap="gray")
        plt.title("Zoomed Grayscale Image")
        plt.show()

    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except ImportError as ie:
        print(f"Import Error: {ie}. Make sure all required libraries are installed.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
