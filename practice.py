"""for x in range(20):
    print(x,("*2="),x*2)

student_score=int(input("your total score"))

if student_score>=70 and student_score<=100:
    print("A")
else:
    print("failed, try again later")

number=int(input("please enter any positive integer"))
if number % 5 and number % 11:
    print(number," is divisible")
else:
    print(number,"is not divisible")


if number % 2:
    print(number, "is an even number")
else:
    print(number,"is an odd number")

for x in range(20):
    print(x,"* 2=",x*2)


class area_circle():
    def __init__(self,pi,radius):
        self.pi=pi
        self.rad=radius
        print(pi*radius)
circ=area_circle(3,5**2)

class cir_circle():
    def __init__(self,pi,radius):
        self.pi=pi
        self.radius=radius
        print(2*pi*radius)
red=cir_circle(3,9)


class novel():
    def __init__(self,title,author,pages,price):
        self.ti=title
        self.au=author
        self.pa=pages
        self.pr=price
        print("the title of the book is",self.ti,"and the author name is",self.au,"the book has",self.pa,"and the selling price is",self.pr)
dov=novel("the gods must be crazy","chinua achebe",300,"$70")



x=novel("listening to God","sam adeniyi",670,1200)
x.printout()

class book(novel):
     def __init__(self,title,author,pages,price):
         novel.__init__(self,title,author,pages,price)
x = novel("listening to God", "sam adeniyi", 670,400)


class book(novel):
    def __init__(self,title,author,pages,price):
        super().__init__(title,author,pages,price)
        self.authorsage= 64
x = novel("listening to God", "sam adeniyi", 670,400)
print(x.authorsage)


class person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print("my name is",self.fname,self.lname)
fro=person("oloruntoba", "favour")

class manager(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
s=manager("alade","johnson")
print()
class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    


class manager(person):
    def __init(self,fname,lname):
        super().__init(self,lname,fname)
        self.graduated = year
u=manager("sunday","adesina",2019)
print()

class family:
    def __init__(self,name,children):
        self.nam=name
        self.child=children
    def family_background(self):
        print("the family of",self.nam,"has",self.child,"children")

fammm=family("Oloruntoba",6)
fammm.family_background()

class child1(family):
    def __init__(self,name,children,age):
        family   .__init__(self,name,children)
        self.ag=age
    def childsview(self):
        print("the family of",self.nam,"has",self.child,"children",self.ag)


red=child1("temitope",4,40)
red.family_background()
red.childsview()

  
import re
fr="the car is good"
free=re.findall("ar",fr)
print(free)

import re
reg="its raining in spanish"
foo=re.sub("raining","snowing",reg)
print(foo)


import re
res="black is the main common type of colour"
froo=re.search("black",res,2)
print(froo)

try:
    print(x)
except:
    print("theres no error")


x=23
try:
    print(x)
except:
    print("error")

try

def table (n,i):
    print(n*1)
    i=i+1
    if i<=10:
        table(n,i)
table(12,1)"""

car={ "brand":"toyota","model":"airspace","year":2019}
car["frouu"]="2013"
car.pop("year")
print(car)
for x in car:
    print(x)

class car():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def printeverything(self):
        print("the car is",self.brand,self.model,"was made in",self.year)


all=car("toyota","camry",2020)
all.printeverything()

class owner(car):
    def __init__(self,brand,model,year):
        car.__init__(self,brand,model,year)
    def everything(self):
        print(self.brand,self.model,self.year)
gijj=owner("favour","shelvron",2030)
gijj.everything()





