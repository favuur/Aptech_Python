

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y


print("select options")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

choice=input("enter your selected options 1,2,3,4")
x=int(input("first digit"))
y=int(input("second digit"))
if choice== "1":
    print(x,"+",y,"=",x+y)
elif choice=="2":
    print(x,"-",y,"=",x-y)
elif choice=="3":
    print(x,"*",y,"=",x*y)
else:
    print(x,"/",y,"=",x/y)




x=int(input("first digit"))
y=int(input("second digit"))

choice=input("+,-,*,/")

if choice=="+":
    print(x,"+",y,"=",x+y)
elif choice=="-":
    print(x, "-",y, "=", x-y)
elif choice=="*":
     print(x, "*",y, "=",x*y)
else:
    print(x,"/",y,"=",x/y)


