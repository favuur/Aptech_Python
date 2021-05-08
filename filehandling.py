'''d=open("trt.txt","a")
d.write("i am a python developer\n")
d.write("working on a file")
d.close()'''

"""import os
os.remove("trust.txt")

if os.path.exist(text.txt):
    print("the ")

t=open("read.txt","a")
t.write("i am a programmer")
t.write("i am good at it")"""


username=input("username")
password=input("password")
phone_number=input("phone number")

details=open("login.txt","w")
details.write("username\n")
details.write("password\n")
details.write(phone_number)
details.close()



