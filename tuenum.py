'''import numpy as gt



#import numpy as gt
print(gt.__version__)
print(type(gt))

arr=gt.array(42)
print(arr)

arr1=gt.array([1,2,3,4,5])
print(arr1)

arr2=gt.array([[1,2,3],[4,5,6]])
print(arr2)


arr3=gt.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr3)

print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)


ar=gt.array([1,2,3,4], ndmin=5)
print(ar)
print("the number of dimension",ar.ndim)

print(arr1[2] + arr1[3])

print(arr2[0,2])
print(arr2[1,2])

ttt=gt.array([[[1,2,3,],[4,5,6]],[[7,8,9],[10,11,12]]])
print(ttt[0,1,2])


import numpy as gr
cat=gr.array([[[2,3,4,5],[6,7,8,9]],[[10,11,12,13],[14,15,16,17]]])
print(cat[1,1,3])
print(cat.dtype)


fruits=gr.array(['apple','mango','cheese','grape'])
print(fruits.dtype)

fri=gr.array([1,2,3,5], dtype='i4')
print(fri.dtype)

new=arr1.astype('f')
print(new)


fro=gr.array([1,2,3,4,5,6,7,8,9,10,11,12])
newfr=fro.reshape(2,3,2)

print(newfr)


for x in arr2:
    #print(x)
  for y in x:
      print(y)


#to loop directly without writing x,y,z use NDITER:
arrg=gr.array([[1,2,3,4],[5,6,7,8]])
for x in gr.nditer(arrg):
    print(x)

bbb=gr.array([1,2,3])
for x in gr.nditer(bbb,flags=['buffered'], op_dtypes=['S']):

    print(x)

for x in gr.nditer(arrg[:, ::3]):
    print(x)

for y, z in gr.ndenumerate(bbb):
    print(y,z)

#concatenate:

arg=gr.array([6,7,8,9,10,11])
agg=gr.concatenate((arr1,arg))
print(agg)

newarr=gr.array_split(arg,3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

x=gr.where(arg==4)
print(x)'''


import numpy as gr

arra=gr.array([41,42,43,44,45])
filter_arr=[]
for x in arra:
    if x > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr=arra[filter_arr]
print(filter_arr)
print(newarr)


arr=gr.array([41,42,43,44])
filter_arr1=arr > 42

newarr1= arr[filter_arr1]

print(newarr1)
print(filter_arr1)

from numpy import random
x=random.randint(1000000)
print(x)


import random
x= random.randrange(100)
print(x)

n=[1,2, 3, 4, 5]

if n% 2==1:
    print(n)



