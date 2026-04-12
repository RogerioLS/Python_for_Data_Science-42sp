import sys


def check_odd_even(number: int):
    """
    This function checks if the given number is odd or even and prints the result.

    Args:
        number (int): The number to be checked.
    
    Returns:
        None: This function does not return anything, it only prints the result.
    """
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


try:
    assert len(sys.argv) <= 2, "more than one argument is provided"

    if len(sys.argv) == 2:
        i_arg = int(sys.argv[1])
        check_odd_even(i_arg)

except AssertionError as e:
    print("AssertionError:", e)
except ValueError:
    print("AssertionError: argument is not an integer")