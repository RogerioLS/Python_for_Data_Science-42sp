import sys


def main():
    """Converts a string to Morse code based on a nested dictionary."""
    NESTED_MORSE = {
        " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ",
        "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
        "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ",
        "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
        "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "
    }

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        arg = sys.argv[1]
        if not isinstance(arg, str):
            raise AssertionError("the arguments are bad")

        res = ""
        for char in arg.upper():
            if char not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
            res += NESTED_MORSE[char]

        print(res.strip())

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
