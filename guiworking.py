"""from tkinter import *
from tkinter import messagebox
school=Tk()
school.title("school")
school.geometry("300x200")


pas=Label(school,text="password",fg="blue").grid(row=0,column=0)
e=StringVar()
e1=Entry(school,textvariable=e).grid(row=0,column=1)

us=Label(school,text="username",fg="blue").grid(row=1,column=0)
eu=StringVar()
eu1=Entry(school,textvariable=eu).grid(row=1,column=1)


def new():
    if e.get()=="" or eu.get()=="":
        messagebox.showerror("error","username or password empty")
    else:
        ap = Tk()
        ap.geometry("500x300")
        ap.title("APTECH")

        ll=Label(ap,text="WELCOME TO APTECH",fg="red").grid()
ll2=Button(school,text="LOGIN",command=new).grid()

mainloop()"""

from tkinter import *
import mysql.connector as dr
from tkinter import messagebox

root = Tk()
root.geometry("1500x900")


def login_in():
    #global login_in
    too = Toplevel(root)
    too.geometry('900x700')

    a = Label(too, text='LOGIN HERE').place(X=9, Y=10)
    a = Label(too, text='USERNAME').place(X=10, Y=70)

    r = StringVar()
    E = Entry(too, textvariable=r).place(X=150, Y=60)
    b = Label(too, text='PASSWORD').place(X=10, Y=140)

    r1 = StringVar()
    E1 = Entry(too, textvariable=r1).place(X=150, Y=130)
    submit = Button(too, text='LOGIN', command=logas).place(X=160, Y=210)

def main():
    head = Label(root, text="welcome to login system").pack()
    log = Button(root, text="LOG IN", command=login_in).pack()

    root.mainloop()
main()

global r
global r1
global e
global e1





def logas():
    global logas
    t = (str(r.get()))
    t1 = (str(r.get()))
    h = (t, t1)
    db = dr.connect('localhost', 'root', 'password', 'database_name')
    cur = db.cursor()
    y = "select * from table office where username=%s and password=%s"
    result = cur.execute(y, h)
    if result == True:
        too = Tk()
        too.geometry('1500x900')
        too.title('login details')
    else:
        ans = messagebox.showerror('error', 'login failed')
        root.quit()
main()