#FUNCTIONS

def fav():
    a=20
    b=30
    c=a+b
    print("the sum of a and b=",c)
fav()


def full():
    a=200
    b=30
    r=60
    c=a-b-r
    print("the subtraction of a from b=",c)
full()

def mul():
    a=170
    b=23
    c=a*b
    print("the multiplication of a and b=",c)
mul()


def div():
    f=int(input("first digit"))
    d=int(input("second digit"))
    x=f/d
    print("f divided by d is",x)
div()




def name(lname,sname):
    print("my name is",lname)

name("ola","favour")



def add(fnumb,snumb):
    t=fnumb+snumb
    print(t)
add(21,31)


#FUNCTIONS WITH DEFAULT PARAMETERS

def mycountry(country="Nigeria"):
    print("i am from",country)

mycountry("Ghana")
mycountry("Togo")
mycountry()
mycountry("Canada")

def myname(lname="favour", fname="ola"):
    print("my first name is",fname)
myname()

def myfamily(*child):
    print("the tallest child name is",child[2])
myfamily("Ade","Joy","Seun","Lola")


def myfamily(child1,child2,child3):
    print("the tallest child name is",child3)
myfamily(child1="sewa",child2="Fola",child3="yemi")

def myfamily(**child):
    print("the tallest child name is",child["child3"])
myfamily(child1="sewa",child2="Fola",child3="yemi")








