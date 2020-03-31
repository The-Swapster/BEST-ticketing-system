from tkinter import *
import sqlite3
import gui1
import gui2
import database


def gui():
    t = Tk()
    t.title('BEST Ticketing System')
    b1 = Button(t, text='Conductor', command=gui2.call_gui2)
    b1.grid(row=0)
    b2 = Button(t, text='Passenger', command=gui1.call_gui1)
    b2.grid(row=1)
    t.mainloop()
    

try:
    database.calls()
    gui()


except sqlite3.IntegrityError:
    gui()
