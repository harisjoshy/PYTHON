#unchangeable, cannot add anything or functions

t= ("apple","orange","banana")
print(type(t))
print(t)
print(t[1])
#to add elements, convert to list

h= list(t)
h[1]="haris"
print(h)
#then convert to tuple
t= tuple(h)
print(t)

t= ("apple","orange","banana")
t1= ("HI","YOU","BYE")
T3= t+t1
print(T3)