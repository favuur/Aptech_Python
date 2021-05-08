"""class Aptech:
    name="oloruntoba favour"
obi=Aptech()
print(obi.name)

class Aptech:
    name="oloruntoba favour"
obi=Aptech()
obi1=Aptech()
print(obi.name)
print(obi1.name)


#INITIALIZE A CLASS
class Aptech:
    def __init__(self,name,age):
        self.nameee=name
        self.ageeee=age
ob2=Aptech("favour",29)
print("my name is",ob2.nameee)
print(ob2.ageeee)



       #OR
class Aptech:
    def __init__(self,name,age):
        self.nameee=name
        self.ageeee=age
    def printout(self):
        print("my name is",self.nameee,"i am ",self.ageeee)
obi1=Aptech("favour",28)
obi1.printout()



class book:
    def __init__(self,author,title,pages,price):
        self.aut=author
        self.tit=title
        self.pag=pages
        self.pri=price
info=book("Chinua Achebe","There was a country",590,"$100")
print("The author of this book is",info.aut)
print("The title of the book is",info.tit)
print("It has",info.pag,"pages")
print("Its selling price is",info.pri)

price=int(input("book price"))
discount=price*0.1
print(discount)


import math
class  circle:
    def __init__(self,radius,pi):
        self.pi = pi
        self.radi=radius
other=circle(3,5)
print(other.pi*other.radi)"""








#INHERITANCE

class Aptech:
    def __init__(self, name, age):
        self.nameee = name
        self.ageeee = age

    def printout(self):
        print("my name is", self.nameee, "i am ", self.ageeee)


obi1 = Aptech("favour", 28)
obi1.printout()


class course(Aptech):
    def __init__(self,name,age,subject):
        Aptech.__init__(self,name,age)
        self.sub=subject
    def pr(self):
        print("the student is studing",self.sub)
cou=course("Remi",50,"python")
cou.printout()


"""str="my string"
r=list(str)
print(r)"""

