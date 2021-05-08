for x in "school":
    print(x)



fruits=["mango","cherry", "banana","apple","grape"]
for x in fruits:

    if x == 'banana':
        break
    print(x)

fruit=["mango","banana","cherry"]
fruit.append("carrot")
print(fruit)



for x in range(1,1000):
    print(x)

#continue
for x in range(5):
    print(x)


fruits=["mango","cherry", "banana","apple","grape"]
for x in fruits:

    if x=="apple":
        continue
    print(x)


for x in range(20):
    print(x,"*2 =",x*2)


for x in range(2,30,2):
    print(x)

for x in range(6):
    print(x)
else:
    print("you are done")


fruits=["mango","cherry", "banana","apple","grape"]

colour=["red","yellow","orange"]
for x in fruits:
    for y in colour:
        print(x,y)


for x in range (1,0,2):
    print(x)

for x in range(30):
    print(x,"*2=",x*2)

num=[1,2,3,45,6,7,8,8,9,9,9,4,3,2,5,6,7]
r=0
for x in num:
    r=r+x
    avg=r/len(num)
print(r)
print("the average value is",avg)
print(len(num))
