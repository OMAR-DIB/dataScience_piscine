from typing import Any


def callLimit(limit: int):
    """
    A decorator that limits the number of times a function can be called.
    """
    count = 0

    def callLimiter(function):
        """
        Inner function that applies the call limit to the decorated function.
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            Wrapper function that tracks function calls and enforces the limit.
            """
            nonlocal count
            count += 1
            if count <= limit:
                return function(*args, **kwds)
            else:
                print(f"Error: <function {function} call too many times")
                # print(f"Error: <function {function.__name__} a\
                #      t {hex(id(function))}>call too many times")
                return
        return limit_function
    # if count > limit:
    #    print(f"Error: <function {function} at\
    #           {hex(id(function))}> call too many times")
    #    exit()
    return callLimiter


# @callLimit(3)
# def f():
# 	print ("f()")
# @callLimit(1)
# def g():
# 	print ("g()")
# for i in range(3):
# 	f()
# 	g()
