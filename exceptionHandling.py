a= 5
b= 6

try:

    print("Resource open")
    print(a/b)
    k = int(input("enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("You cannot divide by zero",e)

except ValueError as e:
    print("value error",e)

except Exception as e:
    print("Invalid entry",e)

finally:
    print("Resourse closed")