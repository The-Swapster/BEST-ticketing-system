from tkinter import *
import sqlite3
import gui
import gui1
import gui2
import database

route_no = ['1 SPL', 'C6Exp']
t4 = Tk()
v3 = StringVar(t4)
v3.set(route_no[0])
w3 = OptionMenu(t4, v3, *route_no)
w3.grid(row=0)
b = Button(t4, text='Next', command=lambda: gui.form(v3.get()))
b.grid(row=1)
t4.mainloop()