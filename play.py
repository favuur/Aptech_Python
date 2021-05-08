'''#QUESTION ONE
e1 =str(input("input alphabet: "))

if e1 == 'a':
    print(e1,"is a vowel")

elif e1 == 'e':
    print(e1,"is a vowel")

elif e1 == 'i':
    print(e1,"is a vowel")

elif e1 == 'o':
    print(e1,"is a vowel")

elif e1 == 'u':
    print(e1,"is a vowel")

else:
    print(e1, "is a CONSONANT")



# QUESTION TWO
re=[]
for x in range(100,400):
    if x%2==0:
        re.append(x)
print(re)


# QUESTION THREE
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area_of_rectangle(self):
        self.aro = self.length * self.width
        print(self.aro)

lit= rectangle(int(input("enter length ")), int(input("enter width ")))

lit.area_of_rectangle()


#QUESTION FOUR
class anything():
    def __init__(self):
        self.strin= ' '
    def get_string(self):
        self.strin = input("write anything")


    def print_string(self):
        print(self.strin)

frr= anything()
frr.get_string()
frr.print_string()


#QUESTION FIVE
class student():
    def __init__(self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name

    def display(self):
        print("student identification number: ",self.student_id, "\n", "student name: ", self.student_name)
stu=student( 1,"Oloruntoba favour")
stu.display()


#QUESTION SIX
question6=input("input to store into a list")
for x in question6:
    for y in x:
        #print(y)
        q6=list(y)
        q66=list(q6)
        print(q66)

#QUESTION
QUESTION7=input("input your text")
print(len(QUESTION7))


#QUESTION
for x in range(1500,2700):
    if x%5==0 and x%7==0:
        print(x)


#QUESTION
question7=str(input("enter your statement"))[::-1]
print(question7)

#QUESTION

question8=int(input("enter your numbers"))
fr=[]
if (question8%2) ==0:

    print(len(question8))
else:
    print("its an odd number",question8)
    print(len( question8))



num=0
while num < 6:
    num+=1
    if (num==3):
        continue
    print(num)'''


datalist=[1452, 11.23, 1+2j, True, 'w3school',(0,-1), [5,12], {"class":'V',"sections":'A'}]
for x in datalist:
    print(x)
    print(type(x))





