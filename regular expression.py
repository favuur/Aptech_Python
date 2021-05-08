import re
check="i am a python developer"
r=re.search("python", check)
print(r)

import re
check="i am a python developer"
r=re.search("^python", check)
print(r)

import re
check="i am a python developer"
r=re.search("python$", check)
print(r)

import re
find="i like coding with python"
ve=re.sub("python","html",find)
print(ve)

import re
find="i like coding with python"
ve=re.sub(" ","%",find)
print(ve)

import re
life="i live in Nigeria"
liv=re.sub("\s","5",life,2)
print(liv)


import re
find="i like coding with python"
ve=re.search("with",find)
print(ve.string)

import re
find="i like coding with python"
ve=re.search("python",find)
print(ve.group())


#to print a set of alphabet
import re
trt="its raining heavily between 6 and 7"
x=re.findall("[a-j]",trt)
z=re.findall("\d",trt)
y=re.findall("r......",trt)
u=re.findall("[a-zA-Z]",trt)
print(x)
print(z)
print(y)
print(u)


