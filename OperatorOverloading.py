
'''Operator overloading in Python is the ability of a single operator
to perform more than one operation based on the class (type) of operands.
 For example, the + operator can be used to add two numbers, concatenate
 two strings or merge two lists'''

class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = student(m1,m2)

        return s3



s1= student(23,58)
s2 = student(26,78)

s3 = s1 + s2

print(s3.m1 + s3.m2)