def square(x: int | float)-> int | float:
    return x**2
def pow(x: int | float)-> int | float:
    return x**x
def outer(x: int | float, function) -> object:
    count = x
    
    def inner() -> float:
        nonlocal count  # This ensures we modify the 'count' variable from the outer function
        count = function(count)  # Calculate the result using the provided function
        return count  # Return the result and the count
    
    return inner


my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())