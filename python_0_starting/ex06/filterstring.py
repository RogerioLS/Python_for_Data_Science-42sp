import sys


def main():
    """
    Filter words by minimum length.

    Returns:
        None
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        # Requisito: ao menos uma list comprehension e um lambda
        words = text.split()
        filtered = [word for word in words if (lambda x: len(x) > n)(word)]
        print(filtered)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
