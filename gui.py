from tkinter import *
import tkinter.font as tkfont
import sqlite3
import gui1
import gui2
import database
import webbrowser


def open(url):
    webbrowser.open_new(url)


def gui(v1):
    t = Toplevel()
    t.title('BEST Ticketing System')
    f = tkfont.Font(family='Sans Serif', size=12)
    img = PhotoImage(file='best_1.png')
    img1 = PhotoImage(file='driver-removebg-preview.png')
    img2 = PhotoImage(file='people_1-removebg-preview.png')
    b3 = Button(t, image=img, command=lambda: open("https://www.bestundertaking.com/in/iis6954.asp?lang=en"))
    Button.image = img
    b3.grid(row=0)
    b1 = Button(t, text='Conductor', image=img1, compound=LEFT, font=f, bg='red3', fg='white', command=lambda :[gui2.call_gui2(v1), t.destroy()])
    b1.image=img1
    b1.grid(row=1, column=1, padx=120, pady=30)
    b2 = Button(t, text='Passenger', image=img2, compound=LEFT, font=f, bg='red3', fg='white', command=lambda :[gui1.call_gui1(v1), t.destroy()])
    b2.image=img2
    b2.grid(row=2, column=1, padx=120, pady=30)


def form(v):
    try:
        database.calls()
        gui(v)

    except sqlite3.IntegrityError:
        gui(v)
