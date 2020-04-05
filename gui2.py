from tkinter import *
import tkinter.font as tkfont
import database as db
import sqlite3
import webbrowser


def open(url):
    webbrowser.open_new(url)

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
        "MH01BA5707"
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
    t2 = Toplevel()
    t2.title("Conductor UI")
    f = tkfont.Font(family='Sans Serif', size=12)
    v1 = StringVar(t2)
    v2 = StringVar(t2)
    img = PhotoImage(file='best_1.png')
    b3 = Button(t2, image=img, command=lambda: open("https://www.bestundertaking.com/in/iis6954.asp?lang=en"))
    Button.image = img
    b3.grid(row=0)
    Label(t2, text="Bus Number", font=f, bg='red3', fg='white').grid(row=1, column=1, padx=30, pady=30, ipadx=15)
    Label(t2, text="Current location", font=f, bg='red3', fg='white').grid(row=2, column=1, padx=30, pady=30)
    if v == "C6Exp":
        v2.set(stopsC6Exp[0])
        w1 = OptionMenu(t2, v2, *stopsC6Exp)
        w1.config(font=f, bg='red3', fg='white')
        w1.grid(row=2, column=3)
        v1.set(C6Exp[0])
        w2 = OptionMenu(t2, v1, *C6Exp)
        w2.config(font=f, bg='red3', fg='white')
        w2.grid(row=1, column=3)
    elif v == "1 SPL":
        v2.set(stops1Spl[0])
        w1 = OptionMenu(t2, v2, *stops1Spl)
        w1.config(font=f, bg='red3', fg='white')
        w1.grid(row=2, column=3, ipadx=5)
        v1.set(spl1[0])
        w2 = OptionMenu(t2, v1, *spl1)
        w2.config(font=f, bg='red3', fg='white')
        w2.grid(row=1, column=3)
    b1 = Button(t2, text="Submit", font=f, bg='red3', fg='white', command=lambda: update_status(v, v1.get(), v2.get()))
    b1.grid(row=3, column=2, padx=30, pady=30, ipadx=45)
