# class computer:
#
#     def __init__(self,cpu,ram):
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("config is ",self.cpu, self.ram)
#
#
# com1 = computer("i3",4) #we are passing 3 values - com1,cpu,ram
# com2 = computer("i5",16)
#
# com1.config()
# com2.config()

class com:

    def __init__(self):
        self.name = "haris"
        self.age = 25

    def compare(self,c):
        if self.age == c.age:
            return True
        else:
            return False

    def update(self):
        self.age=26



c1= com()
c2= com()

c1.name ="HARIS"
c1.age= 26

c2.update()

print(c1.name)
print(c1.age)

if c1.compare(c2):
    print("they are same")
else:
    print("not same")