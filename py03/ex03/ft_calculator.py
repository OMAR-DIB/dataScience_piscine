class calculator:
 #your code here
 def __init__(self,vector):
  self.vector = vector
 def __add__(self, object)-> None:
    for i in range(0,len(self.vector)):
        self.vector[i] += object
    print(self.vector)
 def __mul__(self, object)-> None:
    for i in range(0,len(self.vector)):
        self.vector[i] *= object
    print(self.vector)

 def __sub__(self, object)-> None:
    for i in range(0,len(self.vector)):
        self.vector[i] -= object
    print(self.vector)
 def __truediv__(self, object)-> None:
    for i in range(0,len(self.vector)):
        if object == 0:
            raise ZeroDivisionError('don\'t divise by zero')  
            
        self.vector[i] /= object
    print(self.vector)