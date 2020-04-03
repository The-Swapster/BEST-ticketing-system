from tkinter import *
import database as db
import gui3

Spl1 = [
    "Mumbai CST",
    "Hutatma Chowk",
    "Ahilyabai Holkar Chowk",
    "Mantralay",
    "NCPA"
]

C6Exp = [
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


def call_gui1(v):
    t1 = Tk()
    t1.title("Choose Bus")
    if v == '1 SPL':
        counter = IntVar(t1)
        variable = StringVar(t1)
        variable.set(Spl1[0])
        variable1 = StringVar(t1)
        variable1.set(Spl1[0])
        text3 = Label(t1, text="Source")
        text4 = Label(t1, text="Destination")
        text5 = Label(t1, text="Number of people")
        w = OptionMenu(t1, variable, *Spl1)
        w.grid(row=0, column=4)
        x = OptionMenu(t1, variable1, *Spl1)
        x.grid(row=1, column=4)
        text3.grid(row=0, column=0)
        text4.grid(row=1, column=0)
        text5.grid(row=2, column=0)
        Label(t1, text="Number of people").grid(row=2, column=0)
        Label(t1, textvariable=counter).grid(row=2, column=5)
        Button(t1, text="+", command=lambda: counter.set(counter.get() + 1)).grid(row=2, column=6)
        Button(t1, text="-", command=lambda: counter.set(counter.get() - 1)).grid(row=2, column=4)
        button1 = Button(t1, text='Submit',
                         command=lambda: [gui3.show_entry_fields(variable.get(), variable1.get(), counter.get(), v), t1.destroy()])
        button1.grid(row=8, column=1, pady=4)
    elif v == 'C6Exp':
        counter = IntVar(t1)
        variable = StringVar(t1)
        variable.set(C6Exp[0])
        variable1 = StringVar(t1)
        variable1.set(C6Exp[0])
        text3 = Label(t1, text="Source")
        text4 = Label(t1, text="Destination")
        text5 = Label(t1, text="Number of people")
        w = OptionMenu(t1, variable, *C6Exp)
        w.grid(row=0, column=4)
        x = OptionMenu(t1, variable1, *C6Exp)
        x.grid(row=1, column=4)
        text3.grid(row=0, column=0)
        text4.grid(row=1, column=0)
        text5.grid(row=2, column=0)
        Label(t1, text="Number of people").grid(row=2, column=0)
        Label(t1, textvariable=counter).grid(row=2, column=5)
        Button(t1, text="+", command=lambda: counter.set(counter.get() + 1)).grid(row=2, column=6)
        Button(t1, text="-", command=lambda: counter.set(counter.get() - 1)).grid(row=2, column=4)
        button1 = Button(t1, text='Submit',
                         command=lambda: [gui3.show_entry_fields(variable.get(), variable1.get(), counter.get(), v), t1.destroy()])
        button1.grid(row=8, column=1, pady=4)
