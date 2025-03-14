

def ft_filter(func, iterator):
    """
    Return an iterator yielding those items
    of iterable for which function(item)
    is true. If function is None, return the items that are true.
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
