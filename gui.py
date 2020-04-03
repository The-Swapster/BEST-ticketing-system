from tkinter import *
import sqlite3
import gui1
import gui2
import database


def gui(v1):
    t = Tk()
    t.title('BEST Ticketing System')
    b1 = Button(t, text='Conductor', command=lambda :[gui2.call_gui2(v1), t.destroy()])
    b1.grid(row=0)
    b2 = Button(t, text='Passenger', command=lambda :[gui1.call_gui1(v1), t.destroy()])
    b2.grid(row=1)


def form(v):
    try:
        database.calls()
        gui(v)

    except sqlite3.IntegrityError:
        gui(v)
