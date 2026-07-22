"""Test runner for Exercise 01 (2D Array).

Runs the subject test cases and various error handling validation tests.
"""

from array2D import slice_me


def main() -> None:
    """Tests the slice_me function from array2D."""
    # 1. Subject Test Case
    print("--- Subject Test Case ---")
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    try:
        print(slice_me(family, 1, 3))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print(f"Error during subject test: {e}")

    # 2. Slicing with various indices
    print("\n--- Slicing with various indices ---")
    try:
        print("Full slice (0 to 4):")
        print(slice_me(family, 0, 4))
        print("Negative start (-3 to -1):")
        print(slice_me(family, -3, -1))
        print("Out of bounds slice (0 to 10):")
        print(slice_me(family, 0, 10))
    except Exception as e:
        print(f"Unexpected error: {e}")

    # 3. Error Case: family is not a list
    print("\n--- Error Case: family is not a list ---")
    try:
        slice_me("not a list", 1, 3)
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")

    # 4. Error Case: family contains non-list rows
    print("\n--- Error Case: family contains non-list rows ---")
    try:
        slice_me([[1.80, 78.4], "not a list row"], 0, 1)
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")

    # 5. Error Case: start or end are not integers
    print("\n--- Error Case: start is float ---")
    try:
        slice_me(family, 1.5, 3)
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")

    print("\n--- Error Case: end is boolean (True) ---")
    try:
        slice_me(family, 1, True)
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")

    # 6. Error Case: Inconsistent row sizes
    print("\n--- Error Case: Inconsistent row sizes ---")
    try:
        inconsistent_family = [
            [1.80, 78.4],
            [2.15, 102.7, 99.9],  # Row of length 3
            [2.10, 98.5]
        ]
        slice_me(inconsistent_family, 0, 2)
    except ValueError as e:
        print(f"Caught expected ValueError: {e}")


if __name__ == "__main__":
    main()
