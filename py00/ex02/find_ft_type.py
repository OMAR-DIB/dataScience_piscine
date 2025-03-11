def all_thing_is_obj(object: any)-> int:
    if (type(object) == list):
        print("List :",type(object))
    elif (type(object) == tuple):
        print("Tuple :",type(object))
    elif (type(object) == dict):
        print("Dict :",type(object))
    elif (type(object) == set):
        print("Set :",type(object))
    elif (type(object) == str):
        print(f"{object} is in the kitchen :",type(object))
    else:
        print("Type not found")
    return 42

# ft_tuple = ("Hello", "toto!")
# ft_dict = {"Hello" : "titi!"}
# ft_set = {"Hello", "tutu!"}
 
# all_thing_is_obj(["Hello", "tata!"])
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj(ft_set)
# print(all_thing_is_obj(10))
# all_thing_is_obj("helo")