class Member:
    year=2021
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1

    def relocate(self):
        self.place="place"

    def display(self):
        print("year ",str(Member.year))
        print("name= ", self.name)
        print("age= ",str(self.age))
        print("location= ",self.place)

    @classmethod
    def add_year(cls):
        cls.year=cls.year+1
    @staticmethod
    def add_welcome():
        print("welcome")



h=Member("haris",24,"ekm")
j=Member("paaru",23,"kannur")

Member.add_welcome()

h.display()
j.display()

print("----------------")
Member.add_welcome()

Member.year=Member.year+1

h.add_age()
j.add_age()
h.display()
j.display()



