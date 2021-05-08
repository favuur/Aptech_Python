from tkinter import *
bike=Tk()
bike.title("BIKE INVENTORY")
bike.geometry("700x500")

"""l1=Label(bike,text="bike_Name").grid(row=0,column=0)
ll=Label(bike,text="    ").grid(row=0,column=1)
l2=Label(bike,text="manufacturer").grid(row=0,column=2)
ll1=Label(bike,text="   ").grid(row=0,column=3)
l3=Label(bike,text="state").grid(row=0,column=4)"""


class Bike:
    bike_count = 0
    inventory = []

    def __init__(self, bike_name, manufacturer, state):
        inv = []
        for i in self.inventory:
            inv.append(i.bike_name)
        if bike_name in inv:
            ob = Bike.get(self, bike_name)
            ob.qty += 1
        else:
            self.bike_name = bike_name
            self.manufacturer = manufacturer
            self.state = state
            self.bike_count += 1
            self.inventory.append(self)
            self.qty = 1

    def remove(self, bkname):
        for i in self.inventory:
            if i.bike_name == bkname:
                if i.qty > 1:
                    i.qty -= 1
                    return
                self.inventory.remove(i)
                del i
                self.bike_count -= 1

    def add(self, bike_name, manufacturer, state):
        Bike(bike_name, manufacturer, state)

    def edit(self, prop_to_edit, val):
        self.bike_name = val if prop_to_edit == "bike_name" else self.bike_name
        self.manufacturer = val if prop_to_edit == "manufacturer" else self.manufacturer
        self.state = val if prop_to_edit == "state" else self.state

    def get(self, bkname):
        for i in self.inventory:
            if i.bike_name == bkname:
                return i


    def pr_total(self):
        with open("inv.txt", "w") as f:
            v = ""
            for i  in  self.inventory:
                v += f"Bike Name:  {i.bike_name}, Manufacturer: {i.manufacturer}, Bike: {i.state}, Quantity: {i.qty} \n"
            f.write(v)
            print("Inventory exported successfully !! ")
            print(v)

    def change_state(self, state):
        self.edit("state", state)

bike_add = lambda bkna, man, state : Bike(bkna, man, state)

cv = Bike("gpj-700", "kawasaki", "bought" )
# print(v.bike_name, v.manufacturer, v.state)
#
#
# v.edit("bike_name", "gpg biker 700")
# # v.change_state("sold")
# bike_add("kingo", "Favor ent", "Hired")
# v.remove("kingo")
# v.add("kinotim", "Dami ent", "Bought")
# v.add("kinotim", "Dami ent", "Bought")
# v.remove("kinotim")
# v.edit("state", "Hired")
#
# v.pr_total()

#ll=Button(bike,text="click",command=).pack()
# mainloop()

print("Hello There, Welcome to the bike inventory app")

con=True

def handle(v):
    if v.lower() == "l":
        cv.pr_total()

    if v.lower() == "a":
        bk = input("Input the bike name, manufacturer and state in that order: ")
        bk = bk.split()
        ti = Bike(bk[0], bk[1],bk[2])
        print(f"Added Bike {bk[0]}")

    if v.lower() == "e":
        va = input("Input the bike name prop to edit, a value with a space in between in that order : ")
        va = va.split()
        obk = Bike.get("self", va[0])
        obk.edit(va[1], va[2])
        print(obk.bike_name, obk.manufacturer, obk.state)

    if v.lower() == "r" :
        va = input("Input the bike name to remove: ")
        cv.remove(va)
        cv.pr_total()








while con:
    ans = input("Would you like to see your options: ")
    if ans.lower() == "y" or ans.lower() == "yes":
         v =input("list inventory: 'l' \n Add bikes: 'A' \n Edit a bike 'E' \n Remove a bike 'R' ")
         handle(v)
    else:
         print("This is an invalid input Please Try again!!")
         con = False

# det =Bike()

h=Button(bike,text="EDIT",bg='white',command= lambda: cv.edit("bike_name", "tigerkreniox")).grid(row=7,column=1)
h1=Button(bike,text="REMOVE",bg="white",command= lambda:  cv.pr_total() ).grid(row=7,column=2)
#h2=Button(bike,text="ADD",bg="white",command=add).grid(row=7,column=3)

mainloop()