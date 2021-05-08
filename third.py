"""number=[6788,700,26,1,2,56,35,90,21]
print(len(number))

number=[1,2,56,35,90,21]
print(min(number))
print(max(number))"""


"""number=[1,20,34,567,378]
numbers=[]
print(is_list_empty(number))
print(is_list_empty(numbers))"""

"""number=[700,26,1,2,56,35,90,21]
print(number[0],number[-1])"""

"""FUNKE=["kayode","tolu","prince"]
X=slice(3)
print(FUNKE[X])"""

"""FUNKE=["kayode","tolu","prince"]
FUNKE.reverse()
print(FUNKE)"""

"""wrong
funke = ["kayode","tolu","prince"]
ralph = reversed(funke)
for x in ralph:
print(x)"""

"""FUNKE=["kayode","tolu","prince","kayode"]
x= FUNKE.copy()
print(FUNKE)"""

"""FUNKE=["kayode","tolu","prince"]
num=[1,2,3,4,5,6]
x=FUNKE+num
print(x)

FUNKE=["kayode","tolu","prince"]
print("kayode"not in FUNKE)

FUNKE=["kayode","tolu","prince"]
print("kayode" in FUNKE)"""

"""movie={"director":"tunde kelani","actor":"james brown","light manager":"randy blue"}
movie.pop("actor")
print(movie)"""

"""myfamily={"child1":{"name":"Tunde","age":30}, "child2":{"name":"lekan","age":28}}
print(myfamily["child1"])

myfamily["child1"]["name"]="funke"
print(myfamily)"""

#FROM Key
"""X=("emp1","emp2","emp3")
y=0
z= dict.fromkeys(X,y)
print(z)"""

#if else statement

"""a= 20
b= 2

if a !=b:
  print("The value is not equal")
else:
     print("The statement is wrong")

a=300
b=30

if a >b:
    print("the value of a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("the value of b is greater than a")


username= "aptech"
password= "aptech123"

if username== "aptech" and password=="aptech123":
    print("successful")
else:
    print("error")"""


student_score =int(input("Enter your score"))


if student_score>69 and student_score<100 :
    print("A")
elif student_score>=60 and student_score<=69:
    print("B")
elif student_score>=50 and student_score<=59:
    print("C")
elif student_score>=45 and student_score<=49:
    print("D")
elif student_score>=40 and student_score<=44:
    print("E")
elif student_score<=49 and student_score==0:
    print("F")
else:
    print("error")


"""price=int(input("total price"))
discount=0.1*price
real_cost=price-discount

if price>=10000:
    print("real_cost =",real_cost)
else:
    print("price =",price)"""







