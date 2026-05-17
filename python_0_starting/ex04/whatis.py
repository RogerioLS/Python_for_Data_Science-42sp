import sys


def check_odd_even(number: int) -> None:
    """
    Print whether a number is odd or even.
    """
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main() -> None:
    """
    Parse command-line arguments and validate the input.
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument are provided"

        if len(sys.argv) == 2:
            check_odd_even(int(sys.argv[1]))

    except AssertionError as error:
        print("AssertionError:", error)
    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main()
