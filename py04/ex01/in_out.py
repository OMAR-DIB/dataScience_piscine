def square(x: int | float) -> int | float:
    """
    Calculates the square of a given number.
    """
    return x**2


def pow(x: int | float) -> int | float:
    """
    Raises a number to the power of itself (x^x).
    """
    return x**x


def outer(x: int | float, function) -> object:
    """
    Returns an inner function that repeatedly
    applies the given function to `x`.
    """
    count = x

    def inner() -> float:
        """
        Applies the function to `count`, updates it, and returns the new value.
        """
        nonlocal count
        count = function(count)
        return count

    return inner


# my_counter = outer(3, square)
# print(my_counter())
# print(my_counter())
# print(my_counter())
# print("---")
# another_counter = outer(1.5, pow)
# print(another_counter())
# print(another_counter())
# print(another_counter())
