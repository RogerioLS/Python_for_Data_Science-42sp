"""Unit tests for Module 01 (Array) - 42 Python Piscine."""

import sys
import unittest
import numpy as np
from pathlib import Path

# Add python_1_array subdirectories to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
MODULE_01_DIR = BASE_DIR / "python_1_array"

sys.path.append(str(MODULE_01_DIR / "ex00"))
sys.path.append(str(MODULE_01_DIR / "ex01"))
sys.path.append(str(MODULE_01_DIR / "ex02"))
sys.path.append(str(MODULE_01_DIR / "ex03"))
sys.path.append(str(MODULE_01_DIR / "ex04"))
sys.path.append(str(MODULE_01_DIR / "ex05"))

from give_bmi import give_bmi, apply_limit
from array2D import slice_me
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey


class TestModule01(unittest.TestCase):
    """Test suite for Module 01 exercises."""

    # --- ex00 Tests ---
    def test_ex00_give_bmi_valid(self) -> None:
        """Tests valid BMI calculations."""
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        self.assertIsInstance(bmi, list)
        self.assertAlmostEqual(bmi[0], 22.507863455018317, places=5)
        self.assertAlmostEqual(bmi[1], 29.0359168241966, places=5)
        limits = apply_limit(bmi, 26)
        self.assertEqual(limits, [False, True])

    def test_ex00_give_bmi_errors(self) -> None:
        """Tests error handling for give_bmi."""
        # Mismatched list sizes
        with self.assertRaises(ValueError):
            give_bmi([1.80, 1.75], [80.0])
        # Non-numeric items (strings)
        with self.assertRaises(TypeError):
            give_bmi([1.80, "1.75"], [80.0, 70.0])
        # Booleans (type strictness)
        with self.assertRaises(TypeError):
            give_bmi([True, 1.75], [80.0, 70.0])
        # Non-positive height
        with self.assertRaises(ValueError):
            give_bmi([0.0, 1.75], [80.0, 70.0])

    # --- ex01 Tests ---
    def test_ex01_slice_me_valid(self) -> None:
        """Tests valid 2D slicing."""
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        sliced1 = slice_me(family, 0, 2)
        self.assertEqual(sliced1, [[1.80, 78.4], [2.15, 102.7]])
        sliced2 = slice_me(family, 1, -2)
        self.assertEqual(sliced2, [[2.15, 102.7]])

    def test_ex01_slice_me_errors(self) -> None:
        """Tests error handling for slice_me."""
        # Non-list input
        with self.assertRaises(TypeError):
            slice_me("not a list", 0, 2)
        # Non-integer indices (boolean or string)
        with self.assertRaises(TypeError):
            slice_me([[1, 2]], True, 2)
        # Inconsistent row sizes
        with self.assertRaises(ValueError):
            slice_me([[1, 2], [3]], 0, 2)

    # --- ex02 Tests ---
    def test_ex02_ft_load_valid(self) -> None:
        """Tests loading an existing image."""
        img_path = str(MODULE_01_DIR / "ex02" / "landscape.jpg")
        img_arr = ft_load(img_path)
        self.assertIsInstance(img_arr, np.ndarray)
        self.assertEqual(len(img_arr.shape), 3)
        self.assertEqual(img_arr.shape[2], 3)  # RGB channels

    def test_ex02_ft_load_invalid(self) -> None:
        """Tests error handling for ft_load with invalid path."""
        res = ft_load("nonexistent_file.jpg")
        self.assertIsNone(res)

    # --- ex05 Tests ---
    def test_ex05_pimp_image_filters(self) -> None:
        """Tests image filter outputs and shapes."""
        dummy_img = np.full((10, 10, 3), 100, dtype=np.uint8)

        # Invert
        inv = ft_invert(dummy_img)
        self.assertEqual(inv.shape, (10, 10, 3))
        self.assertEqual(inv[0, 0, 0], 155)

        # Red channel only (G and B cleared)
        red = ft_red(dummy_img)
        self.assertEqual(red.shape, (10, 10, 3))
        self.assertEqual(red[0, 0, 0], 100)
        self.assertEqual(red[0, 0, 1], 0)
        self.assertEqual(red[0, 0, 2], 0)

        # Green channel only (R and B cleared)
        green = ft_green(dummy_img)
        self.assertEqual(green.shape, (10, 10, 3))
        self.assertEqual(green[0, 0, 0], 0)
        self.assertEqual(green[0, 0, 1], 100)
        self.assertEqual(green[0, 0, 2], 0)

        # Blue channel only (R and G cleared)
        blue = ft_blue(dummy_img)
        self.assertEqual(blue.shape, (10, 10, 3))
        self.assertEqual(blue[0, 0, 0], 0)
        self.assertEqual(blue[0, 0, 1], 0)
        self.assertEqual(blue[0, 0, 2], 100)

        # Grey channel
        grey = ft_grey(dummy_img)
        self.assertEqual(grey.shape, (10, 10, 3))
        self.assertEqual(grey[0, 0, 0], 100)
        self.assertEqual(grey[0, 0, 1], 100)
        self.assertEqual(grey[0, 0, 2], 100)


if __name__ == "__main__":
    unittest.main()
