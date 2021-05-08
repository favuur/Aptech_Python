import mysql.connector as sql

from tkinter import *

win = Tk()

win.geometry("500x500")

win.title("Login Page")


def login():
    db = sql.connect(host="localhost", user="root", passwd="")

    cur = db.cursor()

    try:

        cur.execute("create database login")

        db = sql.connect(host="localhost", user="root", passwd="", database="login")

        cur = db.cursor()


    except sql.errors.DatabaseError:

        db = sql.connect(host="localhost", user="root", passwd="", database="login")

        cur = db.cursor()

        try:

            cur.execute("create table main(username varchar(50), NOT NULL, password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass


    finally:

        try:

            cur.execute("create table main(username varchar(50) NOT NULL, "

                        "password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass

    while True:

        user = user1.get()

        passwd = passwd1.get()

        cur.execute("select * from main where username = '%s' and password = %s" % (user, passwd))

        rud = cur.fetchall()

        if rud:

            print("Welcome")

            break


        else:

            cur.execute("insert into main values('{}', {})".format(str(user), passwd))

            db.commit()

            print("Account Created")

            break

    cur.close()

    db.close()


userlvl = Label(win, text="Username :")

passwdlvl = Label(win, text="Password  :")

user1 = Entry(win, textvariable=StringVar())

passwd1 = Entry(win, textvariable=IntVar().set(""))
enter = Button(win, text = "Enter", command = lambda: login(), bd = 0)

enter.configure(bg = "pink")


user1.place(x = 200, y = 220)

passwd1.place(x = 200, y = 270)


userlvl.place(x = 130, y = 220)

passwdlvl.place(x = 130, y = 270)


enter.place(x = 238, y = 325)


win.mainloop()

"""
from tkinter import *
from tkinter import ttk

window=Tk()
window.title('Combobox')
window.geometry('500x250')

def rel():
    le=n.get()
    l4=Label(window,text="your month is " +le).grid()
l1=Label(window,text="GFG Combobox widget",bg="blue",fg='white',font=("Times New Roman",15)).grid(row=0,column=1)
l2=Label(window,text="Select the month:",font=("Times New Roman",10)).grid(row=5,column=0,padx=10,pady=25)

n=StringVar()
monthchoosen= ttk.Combobox(window,width=27,textvariable=n)
monthchoosen['values']= ('January',
                      'February',
                      'March',
                      'April',
                      'May',
                      'June',
                      'July',
                      'August',
                      'September',
                      'October',
                      'November',
                      'December',)


monthchoosen.grid(column=1,row=5)
monthchoosen.current()

l3=Button(window,text="click",command=rel).grid(row=6,column=6)
window.mainloop()
