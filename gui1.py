from tkinter import *
import database as db
import gui3
from functools import partial

spl1 = [
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

def call_gui1():
    t1 = Tk()
    #t1.geometry("325x200")
    t1.title("Choose Bus")
    counter = IntVar(t1)
    variable = StringVar(t1)
    variable.set(spl1[0])
    variable1 = StringVar(t1)
    variable1.set(spl1[0])
    text3 = Label(t1, text="Source")
    text4 = Label(t1, text="Destination")
    text5 = Label(t1, text="Number of people")
    w = OptionMenu(t1, variable, *spl1)
    w.grid(row=0, column=4)
    x = OptionMenu(t1, variable1, *spl1)
    x.grid(row=1, column=4)
    text3.grid(row=0, column=0)
    text4.grid(row=1, column=0)
    text5.grid(row=2, column=0)
    Label(t1, text="Number of people").grid(row=2, column=0)
    Label(t1, textvariable=counter).grid(row=2, column=5)
    Button(t1, text="+", command=lambda: counter.set(counter.get() + 1)).grid(row=2, column=6)
    Button(t1, text="-", command=lambda: counter.set(counter.get() - 1)).grid(row=2, column=4)
    #d = partial(display, variable.get(), variable1.get(), counter.get())
    #button1 = Button(t1, text='Submit', command=d)
    button1 = Button(t1, text='Submit', command=lambda:gui3.show_entry_fields(variable.get(), variable1.get(), counter.get()))
    #print(variable.get(), variable1.get(), counter.get())
    button1.grid(row=8, column=1, pady=4)
    #t.mainloop()

def display(v, v1, c):
    print(v, v1, c)
    s = ''
    for i in range(int(c)):
        l = db.data_entries_passenger(v, v1)
        print(v, v1, a)
        a = "Select * from passenger where ticket_id = ?"
        db.c.execute(a, (l,))
        r = db.c.fetchone()
        s += "Bus Number:" + str(r[0]) + "\nRoute Number: " + str(r[1]) + "\nTicket Id :" + str(
            r[2]) + "\nStart Stop: " + str(r[3]) + "\nEnd Stop: " + str(r[4]) + "\nType: " + str(r[5]) + "\n\n"
        print(s)

#call_gui1()

'''def show_entry_fields(v1, v2, a):
    t.title("Ticket details")
    s = ''
    for i in range(a):
        l = db.data_entries_passenger(v1, v2)
        a = "Select * from passenger where ticket_id = ?"
        db.c.execute(a, (l,))
        r = db.c.fetchone()
        s += "Bus Number:" + str(r[0]) + "\nRoute Number: " + str(r[1]) + "\nTicket Id :" + str(
            r[2]) + "\nStart Stop: " + str(r[3]) + "\nEnd Stop: " + str(r[4]) + "\nType: " + str(r[5]) + "\n\n"
    Label(t, text=s).grid(row=0, column=0)'''


'''def call_gui1():

    t.geometry("325x200")
    t.title("Choose Bus")
    counter = IntVar(t)
    variable = StringVar(t)
    variable.set(spl1[0])
    variable1 = StringVar(t)
    variable1.set(spl1[0])
    button1 = Button(text='Submit', command=gui3.show_entry_fields(variable.get(), variable1.get(), counter.get()))
    button1.grid(row=8, column=1, pady=4)
    text3 = Label(t, text="Source")
    text4 = Label(t, text="Destination")
    text5 = Label(t, text="Number of people")
    w = OptionMenu(t, variable, *spl1)
    w.grid(row=0, column=4)
    x = OptionMenu(t, variable1, *spl1)
    x.grid(row=1, column=4)
    text3.grid(row=0, column=0)
    text4.grid(row=1, column=0)
    text5.grid(row=2, column=0)
    Label(t, text="Number of people").grid(row=2, column=0)
    Label(t, textvariable=counter).grid(row=2, column=5)
    Button(t, text="+", command=lambda: counter.set(counter.get() + 1)).grid(row=2, column=6)
    Button(t, text="-", command=lambda: counter.set(counter.get() - 1)).grid(row=2, column=4)

    t.mainloop()
call_gui1()'''
'''class Gui:
    def __init__(self):
        self.t = Tk()

    def show_entry_fields(self, v1, v2, a):
        self.t.title("Ticket details")
        s = ''
        for i in range(a):
            l = db.data_entries_passenger(v1, v2)
            a = "Select * from passenger where ticket_id = ?"
            db.c.execute(a, (l,))
            r = db.c.fetchone()
            s += "Bus Number:" + str(r[0]) + "\nRoute Number: " + str(r[1]) + "\nTicket Id :" + str(
                r[2]) + "\nStart Stop: " + str(r[3]) + "\nEnd Stop: " + str(r[4]) + "\nType: " + str(r[5]) + "\n\n"
        Label(self.t, text=s).grid(row=0, column=0)
        # self.t.mainloop()

    def call_gui1(self):
        self.t.geometry("325x200")
        self.t.title("Choose Bus")
        counter = IntVar(self.t)
        variable = StringVar(self.t)
        variable.set(spl1[0])
        variable1 = StringVar(self.t)
        variable1.set(spl1[0])
        button1 = Button(text='Submit', command=self.show_entry_fields(variable.get(), variable1.get(), counter.get()))
        button1.grid(row=8, column=1, pady=4)
        text3 = Label(self.t, text="Source")
        text4 = Label(self.t, text="Destination")
        text5 = Label(self.t, text="Number of people")
        w = OptionMenu(self.t, variable, *spl1)
        w.grid(row=0, column=4)
        x = OptionMenu(self.t, variable1, *spl1)
        x.grid(row=1, column=4)
        text3.grid(row=0, column=0)
        text4.grid(row=1, column=0)
        text5.grid(row=2, column=0)
        Label(self.t, text="Number of people").grid(row=2, column=0)
        Label(self.t, textvariable=counter).grid(row=2, column=5)
        Button(self.t, text="+", command=lambda: counter.set(counter.get() + 1)).grid(row=2, column=6)
        Button(self.t, text="-", command=lambda: counter.set(counter.get() - 1)).grid(row=2, column=4)

        # self.t.mainloop()


#g = Gui()
#g.call_gui1()'''
