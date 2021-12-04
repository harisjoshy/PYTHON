#Method Overloading
'''Overloading is the ability of a function or an operator to behave in different ways
 based on the parameters that are passed to the function, or the operands that the operator acts on.'''

class demo:

    def  __init__(self,m1,m2):
        self.m1 =m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s= a+b+c
        elif a!=None and b!=None:
            s =a+b
        else:
            s=a
        return s

s1 = demo(12,55)

print(s1.sum(5))


#METHOD OVERRIDITING
'''Method overriding is an ability of any object-oriented
 programming language that allows a subclass or child class
  to provide a specific implementation of a method that is
 already provided by one of its super-classes or parent classes'''

class Parent:
    def show(self):
        print("Im parent")

class Baby(Parent):
    def show(self):
        print("Baby")

s = Baby()

s.show()
