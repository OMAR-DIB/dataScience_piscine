import sys


MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def main():
    '''
    takes a string as an argument and encodes it into Morse Code.
    '''
    if len(sys.argv) != 2:
        print("AssertionError: the argument should be 2")
        exit(0)

    for i in sys.argv[1]:
        if i.upper() not in MORSE:
            print('AssertionError: the arguments are bad')
            exit()

    print(''.join(MORSE[i.upper()] for i in sys.argv[1]))


if __name__ == "__main__":
    main()
