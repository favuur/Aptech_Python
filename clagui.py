"""import tkinter
win=tkinter.Tk()
win.mainloop()
"""
"""from tkinter import *
win=Tk()
win.title("working with GUI")
win.geometry("300x300")

def click():
    loo=Label(win,text="i am doing well").pack()

boo=Button(win,text="how are you doing today",fg="white",bg="purple",command=click).pack()
#boo.pack()
mainloop()
"""
"""loo=Label(win,text="success in your exams")
loo.grid(column=0,row=0)
loo1=Label(win,text="python")
loo1.grid(column=1,row=2)
loo2=Entry(win)
loo2.grid(column=1,row=3)


loo=Label(win,text="username")
loo.grid(column=0,row=0)
loo1=Entry(win)
loo1.grid(column=1,row=0)
lo=Label(win,text="password")
lo.grid(column=0,row=1)
lo1=Entry(win)
lo1.grid(column=1,row=1)
mainloop()"""



from tkinter import *
from tkinter import messagebox
win=Tk()
win.title("calculator")
win.geometry("300x200")

"""def add():
    num1=t1.get()
    num2=t2.get()
    add=num1+num2
    print(add)
    #print(num1)
    #print(num2)
    l1=Label(win,text=add).pack()


t1=IntVar()
e1=Entry(textvariable=t1).pack()

t2=IntVar()
e2=Entry(textvariable=t2).pack()


b1=Button(win,text="Addition",fg="red",command=add)
b1.pack()
mainloop()


#check botton
def fool():
    l2=Label(text="degree").pack()
l1=Button(text="Education",command=fool).pack()
chk=Checkbutton(win,text="Msc").pack()
chk1=Checkbutton(win,text="Bsc").pack()
chk2=Checkbutton(win,text="Hnd").pack()
chk3=Checkbutton(win,text="Phd").pack()
mainloop()

#LIST
lst = Listbox()
lst.insert(1,"python")
lst.insert(2,"HTML")
lst.insert(3,"java")
lst.pack()

#RADIOBOTTON
rad=Radiobutton(win,text="Female",value=1).pack()
rad=Radiobutton(win,text="Male",value=2).pack()
mainloop()
fun=Label(win,text="NAME")
fun.grid(column=0,row=0)
fun1=Entry(win)
fun1.grid(column=1,row=0)

ss=Label(text="SEX").grid(column=0,row=1)
s=Checkbutton(win,text="Female").grid(column=1,row=1)
s=Checkbutton(win,text="Male").grid(column=1,row=2)



mainloop()

def mes():
    
    messagebox.showinfo("login Detail","are you sure you want to summit")
    messagebox.showinfo("FAQ","who are you")
def er():
    messagebox.showerror("error","check your username and password")

l1=Label(win,text="username").grid()
ll1=Entry(win).grid(row=0,column=1)

l2=Label(win,text="password").grid()
ll2=Entry(win,show="*").grid(row=1,column=1)


b1=Button(win,text="Submit")
b1.place(x=40,y=50)


b2=Button(win,text="Close")
b2.place(x=100,y=50)

if ll1== " " and ll2==" ":
    messagebox.showerror("error","check your username and password")
else:
    messagebox.showinfo("login Detail","are you sure you want to summit")


mainloop()

def roo():

    if t1.get() == "" :
        messagebox.showerror("error","username or password cant be empty")
    else:
        messagebox.showinfo("success","completed")


t=Label(win,text="Username").grid(row=0,column=0)
t1=StringVar()
t11=Entry(win,textvariable=t1).grid(row=0,column=1)

tt=Label(win,text="password").grid(row=1,column=0)
t2=StringVar()
t22=Entry(win,textvariable=t2).grid(row=1,column=1)

t3=Button(win,text="submit",command=roo).grid()

def newpage():
    page=Tk()
    pag=Label(page,text="welcome to Aptech").grid()

but=Button(win,text="login",command=newpage).grid()

mainloop()"""


