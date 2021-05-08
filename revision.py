from tkinter import *
from tkinter import messagebox
app = Tk()
app.title("LOGIN PAGE")
app.geometry("700x400")


def succ():
    userr= defUser.get()
    passw= defPass.get()

    file=open("login_user.txt","w")
    file.write(userr)
    file.write(passw)

    if defUser.get() == "" and defPass.get() == "":
        messagebox.showerror("ERROR", "USERNAME OR PASSWORD INVALID")

    else:
        messagebox.showinfo("successful", "ACCOUNT CREATED SUCCESSFULLY")



def create_user():
    global defUser
    global defPass
    newuser=Tk()
    newuser.title("do anything")
    newuser.geometry("300x200")

    newUser=Label(newuser,text="USERNAME: ",fg="white",bg="black").grid(row=0, column=0)
    defUser=StringVar()
    entryUser=Entry(newuser,textvariable=defUser).grid(row=0, column=1)

    newPass=Label(newuser, text="PASSWORD: ", fg="white", bg="black").grid(row=1, column=0)
    defPass=StringVar()
    entryPass=Entry(newuser,textvariable=defPass).grid(row=1, column=1)

    but_newuser=Button(newuser,text="ENTER", command=succ).grid()



but_login=Button(app,text= "LOGIN", fg="blue", bg= "white" ).pack()
but_create=Button(app,text= "CREATE ACCOUNT", fg="blue", bg= "white",command=create_user ).pack()
details=Label(app,text="If you don't have an account, click on create account").pack()


mainloop()
