from tkinter import *
from tkinter import Canvas
from tkcalendar import *


form=Tk()
form.title("ENQUIRY FORM")
form.geometry('1300x900')

f1=Label(form,text="Date").grid(row=1,column=0)
e1=StringVar()
de=Entry(form,textvariable=e1).grid(row=1,column=1)

f2=Label(form,text='Enquiry NO').grid(row=1,column=2)
e1i=StringVar()
de1=Entry(form,textvariable=e1i).grid(row=1,column=3)

l2=Label(form,text='Name Mr/Mrs/miss :').grid(row=2,column=0)
e2=StringVar()
de2=Entry(form,textvariable=e2).grid(row=2,column=1)

l3=Label(form,text="Address").grid(row=3,column=0)
e3=StringVar()
de3=Entry(form,textvariable=e3).grid(row=3,column=1)
#canvas=Canvas()
#canvas.create_line(5,15,70,15)
#canvas.grid(row=3,column=1)

l4=Label(form,text="Contact no").grid(row=4,column=0)
e4=IntVar()
de4=Entry(form,textvariable=e4).grid(row=4,column=1)

l4i=Label(form,text="Gender").grid(row=4,column=2)
e4i=StringVar()
de4i=Entry(form,textvariable=e4i).grid(row=4,column=3)

l4ii=Label(form,text="date of birth: ").grid(row=4,column=4)
#e4ii=Calendar(form,selectmode="day",year=2021,month=1,day=1).grid(row=4,column=5)
e33=Entry(form).grid(row=4,column=5)

l5=Label(form,text="Email").grid(row=5,column=0)
e5=StringVar()
de5=Entry(form,textvariable=e5).grid(row=5,column=1)

l6=Label(form,text="Parent/Guardian's name: ").grid(row=6,column=0)
e6=StringVar()
de6=Entry(form,textvariable=e6).grid(row=6,column=1)

l6i=Label(form,text="contact's No").grid(row=6,column=2)
e6i=IntVar()
de6i=Entry(form,textvariable=e6i).grid(row=6,column=3)

l7=Label(form,text="EDUCATIONAL QUALIFICATION").grid(row=7,column=0)
l8=Checkbutton(form,text="secondary").grid(row=8,column=0)
l8i=Checkbutton(form,text="High school").grid(row=8,column=1)
l8ii=Checkbutton(form,text="Undergraduate").grid(row=8,column=2)
l9=Checkbutton(form,text="Graduate").grid(row=9,column=0)
l9i=Checkbutton(form,text="Vocational school").grid(row=9,column=1)
l9ii=Checkbutton(form,text="Others").grid(row=9,column=2)
e7=Entry(form).grid(row=9,column=3)


l10=Label(form,text="WOULD YOU LIKE A CAREER IN THE FIELD OF").grid(row=10,column=0)
l10i=Checkbutton(form,text="Marketing").grid(row=11,column=0)
l10ii=Checkbutton(form,text="System Engineer").grid(row=11,column=1)
l10iii=Checkbutton(form,text="Web design").grid(row=11,column=2)
l10iv=Checkbutton(form,text="Software Programming").grid(row=11,column=3)
l11=Checkbutton(form,text="Hardware Networking").grid(row=12,column=0)
l11i=Checkbutton(form,text="Education").grid(row=12,column=1)
l11ii=Checkbutton(form,text="others").grid(row=12,column=2)
l111=Entry(form).grid(row=12,column=3)

L1=Label(form,text="FUTURE PLANS").grid(row=13,column=0)
L2=Checkbutton(form,text="Start your own business").grid(row=14,column=0)
L2i=Checkbutton(form,text="Work as an I.T professional").grid(row=14,column=1)
L2ii=Checkbutton(form,text="Go Abroad").grid(row=14,column=2)
L2iii=Checkbutton(form,text="Others: ").grid(row=14,column=3)

L3=Label(form,text="Do you require placement assistant").grid(row=15,column=0)
L3i=Checkbutton(form,text="YES").grid(row=16,column=0)
L3ii=Checkbutton(form,text="NO").grid(row=16,column=1)

L4=Label(form,text="No. of person in your family in the age group of 17-30 years?").grid(row=17,column=0)
L4I=Checkbutton(form,text="1").grid(row=18,column=0)
L4ii=Checkbutton(form,text="2").grid(row=18,column=1)
L4iii=Checkbutton(form,text="More than 2").grid(row=18,column=2)
L4iv=Checkbutton(form,text="NONE").grid(row=18,column=3)

L5=Label(form,text="NO. of person in your family whose age is below 30 years have passed 12th class or above?").grid(row=19,column=0)
L5i=Checkbutton(form,text="1").grid(row=20,column=0)
L5ii=Checkbutton(form,text="2").grid(row=20,column=1)
L5iii=Checkbutton(form,text="More than 2").grid(row=20,column=2)
L5iv=Checkbutton(form,text="None").grid(row=20,column=3)

L6=Label(form,text="How did you hear about Aptech Computer Education?").grid(row=21,column=0)
L6i=Checkbutton(form,text=" Seminar").grid(row=22,column=1)
L6ii=Checkbutton(form,text="High school").grid(row=22,column=2)
L6iii=Checkbutton(form,text="Undergraduate").grid(row=22,column=3)
L6iv=Checkbutton(form,text="internet").grid(row=23,column=1)
L6v=Checkbutton(form,text="Vocational school").grid(row=23,column=2)
L6vi=Checkbutton(form,text="Others").grid(row=23,column=3)

L7=Label(form,text="Pease write the phone numbers of two other friends/relatives who you feel will be benefited from this academy").grid(row=24,column=0)
L7i=Label(form,text="Name:").grid(row=25,column=0)

L7a=Label(form,text="Phone No.: ")
L7ii=Label(form,text="Email: ").grid(row=26,column=1)




mainloop()

"""

from tkinter import *

#from test import bike

bik=Tk()
bik.title("BIKE COMPANY RECORD")
bik.geometry("500x300")






def addy():
    bike_name=bike_namee.get()
    manufacturer=manufacturerr.get()
    state=statee.get()
    quantity=quantityy.get()


    file = open("bike.txt", "w")
    vb = f"Bike Name: {bike_name}, Manufacturer: {manufacturer}, State: {state}, Quantity: {quantity} "
    file.write(vb)
    # file.write(manufacturer)
    # file.write(state)
    # file.write(quantity)

    label_add=Label(bik,text=vb,bg="white").grid()
    #file.close()



bike_name=str(input("what's the name of the bike "))
manufacturer=str(input("name of the manufacturer "))
state=str(input("input either sold, hired or available "))
quantity=str(input("the quantity "))
list_of_all=f"Bike_name: {bike_name}, Manufacture: {manufacturer}, State: {state}, Quantity: {quantity}"

def listt():

    print(list_of_all)
    label_add = Label(bik, text=list_of_all, bg="white").grid()



label1=Label(bik,text="")

button_add=Button(bik,text="ADD",command=addy).grid()
button_list=Button(bik,text="LIST",command=listt).grid()














mainloop()"""





