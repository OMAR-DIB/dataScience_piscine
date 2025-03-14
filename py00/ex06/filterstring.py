import sys
from ft_filter import ft_filter


def main():
    """
    accepts two arguments: a string(S), and an integer(N).
    The output is a list of words from S
    that have a length greater than N.
    """
    if len(sys.argv) != 3:
        print("AssertionError: the argument should be 3")
        exit(0)
    if not sys.argv[2].isdigit():
        print("AssertionError: argument is not an integer")
        exit()

    arr = sys.argv[1].split(' ')
    nb = int(sys.argv[2])
    # func = lambda x: len(x) > nb
    print(list(ft_filter(lambda x: len(x) > nb, arr)))


if __name__ == "__main__":
    main()
