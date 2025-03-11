# print(filter.__doc__)

def ft_filter(func, iterator):
    """
    filtering elements from an existing iterable based on a given condition
    return true if condition ok false if not ok
    """
    if func:
        for i in iterator:
            if func(i):
                yield i
    else: 
        for i in iterator:
            if i:
                yield i

# words = ["apple", " ",  "" , "banana",   " ", "cherry"]
# print(list(ft_filter(None, words)))
