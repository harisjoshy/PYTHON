'''
SETS ARE UNORDERED COLLECTION OF UNIQUE AND IMMUTABLE OBJECTS.
SETS CAN'T HAVE MULTIPLE  OCCURRENCES LIKE TUPLE AND LIST
'''

set1={"a","b","c","d"}
for i in set1:
    print(i)
print("b" in set1)
#add
set1.add("h")
print(set1)

#update - more than one

set1.update("g","i","j")
print(set1)

#length
print(len(set1))

#remove
set1.remove("j")
print(set1)

#discard
set1.discard("a")
print(set1)

#pop - if nott specified the element, ;last element will deleted
set1.pop()
print(set1)

#delete
#del set1

#CONSTRUCTOR
set2=set(("aa","bb","cc","dd"))
print(set2)

#UNION
set3={1,2,3,4}
set4={2,3,4,5}
#set5= set2.union(set4)
#set5 = set3 | set4
#set3.update(set4) #update with set
print(set3)
set5 = set4-set3
print(set5)

#Sort
lis={1,23,45,67,5,5,1}
t= sorted(lis)
print(t[::-1])

