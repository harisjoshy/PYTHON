import pymysql
x= pymysql.connect(host='localhost',user='root',password='123456789@H',database='haris')
cr= x.cursor()

print("preview data")

cr.execute("select * from sample")

data= cr.fetchone()
print(data)

#for i in data:
   # print(i)

'''value= input(" Enter the keyword:")

cr.execute("select * from sample where name=%s",value)
pl= int(input("enter age to be updated"))

cr.execute("update sample set age=%s where name=%s",(pl,value))'''

dl = input("enter name to delete")
cr.execute("delete from sample where name=%s",dl)
x.commit()
x.close()
