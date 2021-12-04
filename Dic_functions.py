dic={
    1 :"abc",
    2 :"cgd",
    3 :"bjf"
}

dic[""]= int(input("enter value"))

if dic[""]== 1:
    print(dic[1])
elif dic[""] == 2:
    print(dic[2])
elif dic[""]==3:
    print(dic[3])
else:
    print("item not exists")

# print(dic.get(6,"file not found"))

'''unordered, changeable, indexed, key values relationship, {}'''

# dic[1]="Haris"
# print(dic)
#
# for x in dic:
#     print(dic[x])
# if 1 in dic:
#     print("available")
#
# dic[4]= "Karoth"
# print(dic)
#
# dic.pop(1)
# print(dic)
# dic.popitem()
# print(dic)
# del dic[2]
# print(dic)
# dic1= dic.copy()
# print(dic1)

# dictionary using constructor

# new = dict(a="hi",b="hello", c="hey")
# print(new)