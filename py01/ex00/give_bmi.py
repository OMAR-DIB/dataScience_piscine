import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) ->\
        list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for
     each corresponding height and weight pair.
    """
    if not all(isinstance(h, (int, float)) for h in height)\
            or not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("Both height and weight must be\
                          lists of integers or floats.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    height_metre = np.array(height)

    index = 0
    bmi = []
    for i in height:
        bmi.append(weight[index] / (height_metre[index] ** 2))
        index += 1
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a BMI threshold to determine whether each BMI exceeds the limit.
    """
    if not all(isinstance(b, (float, int)) for b in bmi):
        raise ValueError("Both height and weight must be lists\
                          of integers or floats.")
    return (np.array(bmi) > limit).tolist()
