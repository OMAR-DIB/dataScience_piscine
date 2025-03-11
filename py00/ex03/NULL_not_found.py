def NULL_not_found(object: any)-> int:
    # print(float("NaN"))
    if (object == None):
        print("Nothing: None",type(object))
    elif (object == False and type(object)== bool):
        print("Fake: False",type(object))
    elif (object == 0):
        print("Zero: 0",type(object))
    elif (object != object and type(object)== float): # In Python, only NaN is not equal to itself.
        print("Cheese: nan",type(object))
    elif (object == ''):
        print("Empty: ",type(object))
    else:
        print("Type not found")
        return 1
    return 0 