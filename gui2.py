from tkinter import *
import database as db
import sqlite3

stops1Spl = [
    "Mumbai CST",
    "Hutatma Chowk",
    "Ahilyabai Holkar Chowk",
    "Mantralay",
    "NCPA"
]
stopsC6Exp = [
    "Mumbai CST",
    "Hutatma Chowk",
    "Ahilyabai Holkar Chowk",
    "Mantralay",
    "NCPA",
    "Colaba",
    "Dr S P Mukherji Chowk Museum",
    "Lions Gate",
    "Old Custom House",
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

spl1 = ["MH01CD1234",
        "MH01XY6754",
        "MH01MD3245",
        "MH01AB3848",
        "MH01BA5705"
        ]

C6Exp = ["MH01RM5018",
         "MH01UA6550",
         "MH01SA7745",
         "MH01ZM8199",
         "MH01DG1860"
         ]


def update_status(v, v1, v2):
    try:
        db.c.execute("select sum(number) from passenger where end_stop = ?", (v2,))
        count = db.c.fetchone()
        print(count)
        db.c.execute("select count from passenger_count where bus_number = ?", (v1,))
        count1 = db.c.fetchone()
        db.c.execute("update passenger_count set count = ? where bus_number = ?", (count1[0] - count[0], v1))
        db.c.execute('delete from passenger where end_stop = ?', (v2,))
        db.c.execute('Insert into bus_status(bus_number, current_location, passenger_count) Values(?,?,?)', (v1, v2, count1[0] - count[0]))
        db.connection.commit()
    except sqlite3.IntegrityError:
        db.c.execute('update bus_status set current_location = ? where bus_number = ?', (v2, v1))
        db.c.execute("select count(number) from passenger where end_stop = ?", (v2,))
        count = db.c.fetchone()
        db.c.execute("select count from passenger_count where bus_number = ?", (v1,))
        count1 = db.c.fetchone()
        db.c.execute("update passenger_count set count = ? where bus_number = ?", (count1[0] - count[0], v1))
        db.c.execute('delete from passenger where end_stop = ?', (v2,))
        db.connection.commit()


def call_gui2(v):
    t2 = Tk()
    t2.title("Conductor UI")
    v1 = StringVar(t2)
    v2 = StringVar(t2)
    Label(t2, text="Bus Number").grid(row=1, column=0)
    Label(t2, text="Current location").grid(row=2, column=0)
    if v == "C6Exp":
        w1 = OptionMenu(t2, v2, *stopsC6Exp)
        w1.grid(row=2, column=1)
        w2 = OptionMenu(t2, v1, *C6Exp)
        w2.grid(row=1, column=1)
    elif v == "1 SPL":
        w1 = OptionMenu(t2, v2, *stops1Spl)
        w1.grid(row=2, column=1)
        w2 = OptionMenu(t2, v1, *spl1)
        w2.grid(row=1, column=1)
    b1 = Button(t2, text="Submit", command=lambda: update_status(v, v1.get(), v2.get()))
    b1.grid(row=3, column=1)
    t2.mainloop()
