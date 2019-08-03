x=input("Enter a number")
y=input("enter another number")
try:
    z=int(x)/int(y)
    print("x/y =",z)
except Exception as e:
    print("Error :",e)