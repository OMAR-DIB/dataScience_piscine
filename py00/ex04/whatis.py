import sys
def whatis(av):
    if len(av) == 1:
        print("AssertionError: no argument")
        #return AssertionError("no argument")
    elif len(av) > 2:
        print("AssertionError: more than one argument is provided")
    else:
        try:
            number = int(av[1])  
            if (number % 2 == 0):
                print("I'm Even.")
            else :
                print("I'm Odd.")
        except ValueError:
            print("AssertionError: argument is not an integer")

whatis(sys.argv)