#instance methods(accessors&mutators methods), class methods, static methods

class student:

    school = "PYTHON"

    def __init__(self,m1,m2,m3):
        self.m1 =m1
        self.m2= m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def classMethod(cls):
        print("Student Class")

    @staticmethod
    def info():
        print("Static methos")


c1 = student(31,25,65)
c2 = student(26,55,78)

print(c1.avg())
print(student.classMethod())
print(c1.info())