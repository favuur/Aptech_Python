'''for x in "apple":
    print(x)

fruits=["apple","pear","banana","kiwi","mango"]
for y in fruits:
    if y== "banana":
        continue
    print(y)


for x in range(20):
    print(x)

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("finished")


fruits=["apple","pear","banana","kiwi","mango"]
colours=["red","blue","pink","yellow"]

for x in fruits:
    for y in colours:
        print(x,y)

for x in fruits:
    pass

for x in range(1,13):
    print(x)


class circle():
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getCircumference(self):
        return 2*3.14*self.radius

circleD=circle(int(input("enter your radius ")))
print(circleD.radius)
print(circleD.getArea())
print(circleD.getCircumference())


class Student():
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber

    def SetAge(self,age):
        self.age = age


    def setMarks(self,score):
        self.score=score

    def Display(self):
        print(self.name,'ROLL_NO:',self.rollnumber,'AGE:',self.age, 'SCORE:',self.score)


studentD = Student(input("enter your name"), input("enter you roll_number"))
print(studentD.SetAge(int(input("enter you age"))))
print(studentD.setMarks(input("enter you score")))
print(studentD.Display())



class Time():
    def __init__(self,hours,minutes):
        self.hours= hours
        self.minutes= minutes
    def addTime(t1,t2):
        t3=Time(0,0)
        t1.minutes`



times=Time(4,41)
print(times.add


frr=[1,2,4,6,5,7,8]
des=[]
res=[]
for x in frr:
    if x % 2 == 0:
        des.append(x)
    else:'''



passw
