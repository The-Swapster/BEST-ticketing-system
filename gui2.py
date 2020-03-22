from tkinter import *
import database_1 as db
import sqlite3
t=Tk()
t.title("Conductor UI")
stops =[
    "Mumbai CST",
    "Hutatma Chowk",
    "Ahilyabai Holkar Chowk",
    "Mantralay",
    "NCPA",
    "Colaba",
    "Dr S P Mukherji Chowk Museum",
    "Lions Gate",
    "'Old Custom House",
    "RBI Fort",
    "Swami D Saraswati Chowk Fort",
    "Carnac Bander",
    "Wadi Bander",
    "Jijamata Nagar",
    "Acharya Vidyaniketan",
    "H P Nagar",
    "Bpcl Sports Club Mahul",
    "Shankar Mandir",
    "Vashi Naka",
    "Aziz Baug",
    "Marawali Baug",
    "Chembur Colony",
    "Navjeevan Society (Chembur)",
    "Basant Park",
    "Chembur Naka Swami Vivekanand Chowk",
    "Sandu Wadi",
    "Acharya Gardendiamond Garden",
    "10th Road Chembur Church",
    "Dr. Ambedkar Garden"
]
busno=[ "MH01CD1234",
        "MH01XY6754",
        "MH01MD3245",
        "MH01AB3848",
        "MH01BA5705",
        "MH01RM5018",
        "MH01UA6550",
        "MH01SA7745",
        "MH01ZM8199",
        "MH01DG1860"
]
v1=StringVar(t)
v1.set(stops[0])
v2=StringVar(t)
v2.set(busno[0])

def update_status():
    db.c.execute('Insert into bus_status(bus_number,current_location) Values(?,?)',(v1.get(),v2.get()))
    db.connection.commit()

Label(t,text="Bus Number").grid(row=0,column=0)
Label(t,text="Current location").grid(row=1,column=0)
w1=OptionMenu(t,v1,*stops)
w1.grid(row=1,column=1)
w2=OptionMenu(t,v2,*busno)
w2.grid(row=0,column=1)
b1=Button(t,text="Submit",command=update_status)
b1.grid(row=2,column=1)

t.mainloop()
