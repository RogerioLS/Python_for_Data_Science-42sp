"""Module to load an image, slice, manually transpose, and display it."""

import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main() -> None:
    """Loads animal.jpeg, slices a 400x400 region, transposes it manually,

    prints shapes and contents, and displays the transposed image.
    """
    try:
        # Load the image
        img = ft_load("animal.jpeg")
        if img is None:
            raise FileNotFoundError("Image 'animal.jpeg' could not be loaded.")

        # Slice the 400x400 region from the image with 1 color channel
        # The slice coordinates 100:500 (height) and 380:780 (width) target the raccoon
        sliced = img[100:500, 380:780, 0:1]

        # Print the shape and content of the sliced image
        print(f"The shape of image is: {sliced.shape} or {sliced.shape[:2]}")
        print(sliced)

        # Transpose the sliced array manually using nested loops
        height, width, _ = sliced.shape
        # Create a new array to store the transposed image
        transposed = np.zeros((width, height), dtype=sliced.dtype)

        for i in range(height):
            for j in range(width):
                transposed[j, i] = sliced[i, j, 0]

        # Print the shape and content after transpose
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)

        # Display the transposed grayscale image using matplotlib
        plt.imshow(transposed, cmap="gray")
        plt.title("Transposed Grayscale Image")
        plt.show()

    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}")
    except ImportError as ie:
        print(f"Import Error: {ie}. Make sure all required libraries are installed.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
