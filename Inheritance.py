'''
INHERITANCE - without doing any modification on existing class , it creates a new class
PARENT (BASE CLASS) & CHILD CLASS(DERIVED CLASS)
IT ALLOWS US TO DEFINE A CLASS THAT INHERITS ALL ,METHODS AND PROPERTIES FROM ANOTHER CLASS

1. SINGLE INHERITANCE  - SINLE DERIVED CLASS INHERITS FROM ANOTHER PARENT CLASS  A > B
2. MULTILEVEL INHERITANCE - PARENT > INTERMEDIATORY CLASS > DERIVED CLASS A > B > C
3. MULTIPLE INHERITANCE - INHERITATION OF CLASS FROM MULTIPLE CLASSES WITH NO CONNECTIONS   A< C > B
4. HIERARCHICAL (HYBRID) INHERITANCE - COMBINATION OF ALL ABOVE INHERITANCES

ENCAPSULATION - WRAPPING UP OF DATA INTO SINGLE UNIT
'''


class A:
    def __init__(self, name,hodname): #self is keyword any word can be used
        self.name= name
        self.hodname = hodname

class B(A):
    def putdata(self):
        self.name = input("name")
        self.hodname = input("HOD name")
    def Display(self):
        print("std name", self.name)
        print("hod",self.hodname)

#obj= A("","") #inheritance
#obj.putdata()
#obj.Display()

#MULILEVEL INHERITANCE

class C(B):
    def fun(self):
        print("Class C")
class D(C):
    def fun1(self):
        print("class D")


obj= D("","") #multilevel inheritance
obj.putdata()
obj.Display()
obj.fun()
obj.fun1()

#MULTIPLE INHERITANCE

class D :
    def get1(self):
        print("Class A")
class E:
    def get2(self):
        print("Class B")

class F(D,E):
    def put(self):
        print("inherited from D&E")
obj = F()
obj.get1()
obj.get2()
obj.put()

#HYBRID INHERITANCE -COMBINATION OF ALL INHERITANCES