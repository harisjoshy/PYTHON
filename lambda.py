# one expression with several arg - AnoNYMOUS fn

x= lambda a:a+2
print(x(5))

x= lambda a,b : a*b+8
print(x(5,2))



def mul(n):
    return lambda a: a*n

n = mul(11)
print(n(5))
m = mul(8)
print(n(8))

# EXCECUTED WITH ONE EXPRESSION, FN WITHOUT NAME -  THROW AWAY FNS -  