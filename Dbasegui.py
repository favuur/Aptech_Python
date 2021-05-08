from tkinter import *
from tkinter import messagebox
import mysql.connector as co


win=Tk()
win.title("LOGIN TO DATABASE")
win.geometry('400x300')

def log():
    t=r.get()
    t1=u.get()
    if t=="" and t1=="":
        print("username and password cannot be empty")
        messagebox.showerror("ERROR", "check username or password")

    else:
        mydb=co.connect(host="localhost",user="root",password="",database="office")
        tr=mydb.cursor()
        sql="select * from file where username=%s and password=%s "
        val=(t,t1)
        tr.execute(sql,val)
        myresult=tr.fetchall()
        for x in myresult:
            messagebox.showinfo("successful","login successful")
        else:
            messagebox.showerror("error","username or password is not correct")


y1=Label(win,text="USERNAME: ",bg="blue").grid(column=0,row=0)
r=StringVar()
r1=Entry(win,textvariable=r).grid(column=1,row=0)

l2=Label(win,text="PASSWORD: ",bg="blue").grid(column=0,row=1)
u=StringVar()
u1=Entry(win,textvariable=u).grid(column=1,row=1)

b=Button(win,text="LOGIN",command=log).grid(column=5,row=5)

mainloop()