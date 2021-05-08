a= lambda b:b*10
print(a(6))

a= lambda b,e:b*e
print(a(6,7))

a= lambda b,e,f:b*e+f
print(a(6,7,90))

#DOUBLE FUCTIONS
def num(n):
    return lambda a:n*a
num1=num(3)
print(num1(22))



#scope, local variable and global variable
a=20
def mynum():
    a=40
mynum()
print(a)



a=20
def mynum():
    global a
    a=40
mynum()
print(a)


a=70
def mynum():
    a=40
    def mynum2():
        print(a)
    mynum2()
mynum()
print(a)


a=70
def mynum():
    global a
    a=40
    def mynum2():
        print(a)
    mynum2()
mynum()
print(a)








