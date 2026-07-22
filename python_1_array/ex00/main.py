from give_bmi import give_bmi, apply_limit


def main() -> None:
    """Test function to run the Give my BMI exercise."""
    # 1. Subject Test Case
    print("--- Subject Test Case ---")
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except Exception as e:
        print(f"Error during subject test: {e}")

    # 2. Error Case: Different sizes
    print("\n--- Error Case: Different list sizes ---")
    try:
        give_bmi([1.80, 1.75], [80.0])
    except ValueError as e:
        print(f"Caught expected ValueError: {e}")

    # 3. Error Case: Non-numeric elements
    print("\n--- Error Case: Non-numeric elements ---")
    try:
        give_bmi([1.80, "1.75"], [80.0, 70.0])
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")

    # 4. Error Case: Non-numeric limits
    print("\n--- Error Case: Non-numeric limit in apply_limit ---")
    try:
        apply_limit([22.5, 25.0], "26")
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")

    # 5. Error Case: Zero or negative values
    print("\n--- Error Case: Zero height ---")
    try:
        give_bmi([0.0, 1.75], [80.0, 70.0])
    except ValueError as e:
        print(f"Caught expected ValueError: {e}")


if __name__ == "__main__":
    main()
