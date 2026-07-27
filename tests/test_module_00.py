"""Unit tests for Module 00 (Starting) - 42 Python Piscine."""

import math
import sys
import unittest
from pathlib import Path

# Add python_0_starting to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
MODULE_00_DIR = BASE_DIR / "python_0_starting"

sys.path.append(str(MODULE_00_DIR / "ex02"))
sys.path.append(str(MODULE_00_DIR / "ex03"))
sys.path.append(str(MODULE_00_DIR / "ex06"))
sys.path.append(str(MODULE_00_DIR / "ex08"))

from find_ft_type import all_thing_is_obj
from NULL_not_found import NULL_not_found
from ft_filter import ft_filter
from Loading import ft_tqdm


class TestModule00(unittest.TestCase):
    """Test suite for Module 00 exercises."""

    def test_ex02_find_ft_type(self) -> None:
        """Tests type detection in ex02."""
        self.assertEqual(all_thing_is_obj([1, 2]), 42)
        self.assertEqual(all_thing_is_obj((1, 2)), 42)
        self.assertEqual(all_thing_is_obj({"a", "b"}), 42)
        self.assertEqual(all_thing_is_obj({"a": 1}), 42)
        self.assertEqual(all_thing_is_obj("Brian"), 42)
        self.assertEqual(all_thing_is_obj(10), 42)

    def test_ex03_null_not_found(self) -> None:
        """Tests null-like value detection in ex03."""
        self.assertEqual(NULL_not_found(None), 0)
        self.assertEqual(NULL_not_found(float("nan")), 0)
        self.assertEqual(NULL_not_found(0), 0)
        self.assertEqual(NULL_not_found(""), 0)
        self.assertEqual(NULL_not_found(False), 0)
        self.assertEqual(NULL_not_found("Hello"), 1)
        self.assertEqual(NULL_not_found(42), 1)

    def test_ex06_ft_filter(self) -> None:
        """Tests custom ft_filter function against Python filter behavior."""
        sample_list = [0, 1, 2, False, 3, "", "hello", None]
        # Test with None function
        result_none = list(ft_filter(None, sample_list))
        expected_none = list(filter(None, sample_list))
        self.assertEqual(result_none, expected_none)

        # Test with custom lambda predicate
        is_even = lambda x: isinstance(x, int) and x % 2 == 0
        result_even = list(ft_filter(is_even, [1, 2, 3, 4, 5, 6]))
        expected_even = list(filter(is_even, [1, 2, 3, 4, 5, 6]))
        self.assertEqual(result_even, expected_even)

    def test_ex08_ft_tqdm(self) -> None:
        """Tests progress bar generator yielding all items in range."""
        input_range = range(10)
        output_list = list(ft_tqdm(input_range))
        self.assertEqual(output_list, list(input_range))


if __name__ == "__main__":
    unittest.main()
