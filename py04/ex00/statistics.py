from typing import Any
import numpy as np


def mean(array):
    """
    Calculate the mean (average) of a given list of numbers.
    """
    return sum(array) / len(array)


def median(array) -> float:
    """
    Compute the median value of a given list.
    """
    sort = sorted(array)
    middle = (len(sort) - 1) // 2  # Find middle index
    if len(sort) % 2 == 0:
        return float(mean([sort[middle], sort[middle + 1]]))
    else:
        return float(sort[middle])


def quartile(data):
    """
    Compute the first (Q1) and third (Q3) quartiles of a dataset.
    :param data: List of numerical values.
    :return: List containing Q1 and Q3.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)
    q1_index = 0.25 * (n - 1)
    q3_index = 0.75 * (n - 1)

    def get_value(index, sorted_data):
        """
        Compute interpolated quartile value if needed.
        """
        lower = int(index)
        fraction = index - lower
        if lower + 1 >= len(sorted_data):
            return sorted_data[lower]
        else:
            return sorted_data[lower] * (1 - fraction)\
                    + sorted_data[lower + 1] * fraction

    q1 = get_value(q1_index, sorted_data)
    q3 = get_value(q3_index, sorted_data)
    return [q1, q3]


def var(data):
    """
    Compute the variance of a dataset.
    """
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def std_dev(data):
    """
    Compute the standard deviation of a dataset.
    """
    return var(data) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Compute various statistics (mean, median, quartile,
      std deviation, variance) based on keyword arguments.
    """
    if not args:
        for _ in kwargs:
            print("ERROR")
        return

    try:
        data = np.array(args)
        # print(data)
    except Exception as e:
        print(f'Error: {e}')
        exit()
    results = {}
    for key, value in kwargs.items():
        if value == "mean":
            results[value] = mean(data)
        elif value == "median":
            results[value] = int(median(data))
        elif value == "quartile":
            results[value] = quartile(data)
        elif value == "std":
            results[value] = std_dev(data)
        elif value == "var":
            results[value] = var(data)

    if results:
        for key, value in results.items():
            print(f"{key} : {value}")

    # else:
        # print("ERROR")
        # print("ERROR")
        # print("ERROR")
# def ft_statistics(*args: Any, **kwargs: Any) -> None:
#    if not args:
#        print("ERROR")
#        print("ERROR")
#        print("ERROR")
#        return
#    try:
#        data = np.array(args)
#        # print(data)
#    except:
#        print("Error")
#        exit(0)
#    results = {}
#    for key, value in kwargs.items():
#        if value == "mean":
#            results[value] = np.mean(data)
#        elif value == "median":
#            results[value] = np.median(data)
#        elif value == "quartile":
#            results[value] =
#  [np.percentile(data, 25), np.percentile(data, 75)]
#        elif value == "std":
#            results[value] = np.std(data, ddof=0)
#        elif value == "var":
#            results[value] = np.var(data, ddof=0)
#    if results:
#        for key, value in results.items():
#            print(f"{key} : {value}")
#    # else:
#        # print("ERROR")
#        # print("ERROR")
#        # print("ERROR")
