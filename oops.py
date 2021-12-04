'''
CLASS - USER DEFINED PROTOTYPE / BLUEPRINTS FOLLOWED BY OBJTS  - LOGICAL STRUCTURE
OBJ- INSTANCE OF CLASS - PHYSICAL ENTITY
ONLT WITH OBJS WE CAN ACCESS THE DATA & FNS

'''

class student:
    def __init__(self, name,mark): #self is keyword any word can be used
        self.name= name
        self.mark= mark
    def getData(self):
        self.name=input("enter name")
        self.mark=input("mark")
    def putData(self):
        print(self.name,"\n", self.mark)

obj= student("","")
obj.getData()
obj.putData()

#ENCAPSULATION = WRAPPING UP OF DATA IN TO SINGLE UNIT
