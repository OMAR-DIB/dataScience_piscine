import sys


def building(str):
    """
    we use dictionary to avoid the huge nb of variables
    we use ascii code because we cannot import string library
    the ord function convert character to ascii
    """
    counts = {
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0
    }
    for char in str:
        ascii_code = ord(char)
        # punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        if 65 <= ascii_code <= 90:
            counts["upper"] += 1
        elif 97 <= ascii_code <= 122:
            counts["lower"] += 1
        elif 48 <= ascii_code <= 57:
            counts["digits"] += 1
        elif ascii_code == 32:
            counts["spaces"] += 1
        elif (33 <= ascii_code <= 47) or (58 <= ascii_code <= 64)\
                or (91 <= ascii_code <= 96) or (123 <= ascii_code <= 126):
            counts["punctuation"] += 1

    return counts


def main():
    """
    the main to call the building function and manage args and output
    """
    if len(sys.argv) > 2:
        raise AssertionError("Too many arguments provided.")
    if len(sys.argv) == 2:
        string = sys.argv[1]
        counts = building(string)
        print(f"The text contains {len(string)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")
    else:
        string = input("What is the text to count?\n")
        counts = building(string)
        print(f"The text contains {len(string) + 1} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces'] + 1} spaces")
        print(f"{counts['digits']} digits")


if __name__ == "__main__":
    main()
