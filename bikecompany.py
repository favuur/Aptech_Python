from tkinter import *

#from test import bike

bik=Tk()
bik.title("BIKE COMPANY RECORD")
bik.geometry("500x300")


def addy():
    bike_name= bike_nam.get()
    manufacturer= manufacture.get()
    state= stat.get()
    quantity= quantit.get()

    file = open("bike.txt", "a")
    vb = f"'Bike Name:' {bike_name}, 'Manufacturer:' {manufacturer}, 'State:' {state}, 'Quantity:' {quantity}"
    file.write(vb)
    file.close()
    print(vb)
    label_add=Label(bik,text=vb,bg="white").grid()

def listt():
    print(list_of_all)
    label_add = Label(bik, text=list_of_all, bg="white").grid()



label_n=Label(bik,text="bike_name",bg="white").grid(row=0,column=0)
label_m=Label(bik,text="Manufacturer",bg="white").grid(row=0,column=1)
label_s=Label(bik,text="State",bg="white").grid(row=0,column=2)
label_q=Label(bik,text="Quantity",bg="white").grid(row=0,column=3)

bike_nam=StringVar()
entry_b=Entry(bik,textvariable="bike_nam").grid(row=1,column=0)

manufacture=StringVar()
entry_m=Entry(bik,textvariable="manufacture").grid(row=1,column=1)

stat=StringVar()
entry_s=Entry(bik,textvariable="stat").grid(row=1,column=2)

quantit=StringVar()
entry_q=Entry(bik,textvariable="quantit").grid(row=1,column=3)

button_add=Button(bik,text="ADD",command=addy).grid(row=5,column=0)
button_list=Button(bik,text="LIST",command=listt).grid(row=5,column=1)
button_edit=Button(bik,text="EDIT").grid(row=5,column=2)
button_remove=Button(bik,text="EDIT").grid(row=5,column=3)

mainloop()
