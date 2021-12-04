'''
SPECIAL TYPE OF SEQUENCE OF CHARACTERS TO RECOGNISE OTHER STRINGD OR SETS OF STRINGS
BY USING A SPECIALIZED SYNTAX HELD IN PATTERN

REGULAR EXPRESSSION OR RegEx- re MODULE IS USED
'''

import re
pattern=r"haris"

#if re.match(pattern,"hai haris joshy"):
   # print("match")
#else:
 #   print("not match")

#if re.search(pattern,"hai harisjoshy"):
    #print("match")
#else:
   # print("not match")

#FINDALL - RETURNS A LIST CONTAINING ALL MATCHES
print(re.findall(haris,"harisjosy harisjosyharisjosyharisjosyharisjosyharisjosyharisjosyv"))

#SUB - REPLACES ONE OR MANY MATCHES WITH A STRING
str= "haris is smart"
pattern=r"haris"
new=re.sub(pattern,"HARIS",str)
print(new)

#DOT MATCH
str =  r"Ha.is."
if re.match(str,"Harisj"):
    print("match")
else:
    print("not match")
# CHARACTER CLASS\
pattern=r"[A-z][a-z][0-9]"
if re.search(pattern,"Av5"):
    print("corrected")