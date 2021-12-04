class A:
    def __init__(self):
        print("class A init")
    def feature(self):
        print("Feature 1")
class B:
    def __init__(self):
        print("Class B init")
    def feature(self):
        print("feature B ")

class C(A,B):

     def __init__(self):
         super().__init__()  #SUPER CLASS
         print("class c init")


c = C()

#METHOD RESOLUTION ORDER - LEFT TO RIGHT