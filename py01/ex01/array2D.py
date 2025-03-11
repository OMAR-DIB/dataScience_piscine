import numpy as np

def slice_me(family: list, start: int, end: int)-> list:
    if np.array(family).ndim != 2:
        return TypeError("family must be a list of a list")
    if not isinstance(start, int) or not isinstance(end, int):
        return TypeError("start and end must be integers")
    """
    The set() function takes the generator expression and creates a set from the yielded row lengths. A set is a collection of unique elements.
    If all rows have the same length, the set will contain only one element (the common length).
    If the rows have different lengths, the set will contain multiple elements (the different lengths)
    """
    if len(set(len(row) for row in family)) > 1:
        return ValueError("All rows in family must have the same length")
    
    array = np.array(family)
    print("My shape is :",array.shape)
    new_shape = array[start:end,0:]
    print("My new shape is :",new_shape.shape)
    return new_shape

family = [[1.80, 78.4],
 [2.15, 102.7],
 [2.10, 98.5],
 [1.88, 75.2]]
print(slice_me(family, 0, 8))
print(slice_me(family, 1,-2))