from typing import Any
from typing import Any
import numpy as np

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    if not args:
        print("ERROR")
        print("ERROR")
        print("ERROR")
        return
    
    try:
        data = np.array(args)
        # print(data)
    except:
        print("Error")
        exit(0)
    results = {}
    for key, value in kwargs.items():
        if value == "mean":
            results[value] = np.mean(data)
        elif value == "median":
            results[value] = np.median(data)
        elif value == "quartile":
            results[value] = [np.percentile(data, 25), np.percentile(data, 75)]
        elif value == "std":
            results[value] = np.std(data, ddof=0)
        elif value == "var":
            results[value] = np.var(data, ddof=0)
    
    if results:
        for key, value in results.items():
            print(f"{key} : {value}")
    # else:
        # print("ERROR")
        # print("ERROR")
        # print("ERROR")
        
        
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")