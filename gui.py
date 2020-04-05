from tkinter import *
import tkinter.font as tkfont
import sqlite3
import gui1
import gui2
import database


def gui(v1):
    t = Tk()
    t.title('BEST Ticketing System')
    f = tkfont.Font(family='Sans Serif', size=12)
    b1 = Button(t, text='Conductor', font=f, bg='red3', fg='white', command=lambda :[gui2.call_gui2(v1), t.destroy()])
    b1.grid(row=0, padx=120, pady=30)
    b2 = Button(t, text='Passenger', font=f, bg='red3', fg='white', command=lambda :[gui1.call_gui1(v1), t.destroy()])
    b2.grid(row=1, padx=120, pady=30)


def form(v):
    try:
        database.calls()
        gui(v)

    except sqlite3.IntegrityError:
        gui(v)
