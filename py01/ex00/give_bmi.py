import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float])-> list[int | float]:
    if not all(isinstance(h, (int, float)) for h in height) or not all(isinstance(w, (int, float)) for w in weight):
        return ValueError("Both height and weight must be lists of integers or floats.")
    if len(height) != len(weight):
        return ValueError("Height and weight lists must be of the same length.")
    height_metre = np.array(height) / 100

    index = 0
    bmi = []
    for i in height:
        bmi.append(weight[index] / (height_metre[index] ** 2))
        index+=1
    return bmi

def apply_limit(bmi: list[int | float], limit: int)-> list[bool]:
    if not all(isinstance(b,(float,int) ) for b in bmi):
        return ValueError("Both height and weight must be lists of integers or floats.")
    return (np.array(bmi) > limit).tolist()


print(give_bmi(["hi",162,189],[90,80,89]))
print(apply_limit(give_bmi([176,162,189],[90,80,89]),28))