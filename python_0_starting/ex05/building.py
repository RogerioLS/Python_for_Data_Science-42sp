import string
import sys


def validate_arguments(arguments: list[str]) -> str:
    """
    Validate the command-line arguments.

    Args:
        arguments (list[str]): Command-line arguments.

    Returns:
        str: The text to analyze.

    Raises:
        AssertionError: If more than one argument is provided.
    """
    if len(arguments) == 0:
        print("What is the text to count?")
        return sys.stdin.readline()
    if len(arguments) > 1:
        raise AssertionError("more than one argument is provided")
    return arguments[0]


def count_types(text: str) -> dict[str, int]:
    """
    Count character categories in the text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict[str, int]: Counts for each character category.
    """
    types = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0,
    }

    for char in text:
        if char.isupper():
            types["upper"] += 1
        elif char.islower():
            types["lower"] += 1
        elif char in string.punctuation:
            types["punctuation"] += 1
        elif char.isspace():
            types["spaces"] += 1
        elif char.isdigit():
            types["digits"] += 1

    return types


def main():
    """
    Run the program.
    """
    try:
        arguments = sys.argv[1:]
        text = validate_arguments(arguments)

        types = count_types(text)

        print(f"The text contains {len(text)} characters:")
        print(f"{types['upper']} upper letters")
        print(f"{types['lower']} lower letters")
        print(f"{types['punctuation']} punctuation marks")
        print(f"{types['spaces']} spaces")
        print(f"{types['digits']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
