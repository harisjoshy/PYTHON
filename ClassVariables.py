class car:
    wheel = 4 #class namespace, class/static variables

    def __init__(self):
        self.name = "BMW"  #instance namespace , instance variables
        self.milega =10

c1=car()
c2 =car()

#car.wheel= 6

print(c1.name,c2.wheel)