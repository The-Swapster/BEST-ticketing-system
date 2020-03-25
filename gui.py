from tkinter import *
import gui1
import gui2
import database

try:
    t = Tk()
    t.title('BEST Ticketing System')
    database.calls()
    Button(t, text='Conductor', command=gui2.call_gui2).pack()
    Button(t, text='Passenger', command=gui1.call_gui1).pack()
    t.mainloop()

except:
    t = Tk()
    t.title('BEST Ticketing System')
    Button(t, text='Conductor', command=gui2.call_gui2()).pack()
    Button(t, text='Passenger', command=gui1.call_gui1()).pack()
    t.mainloop()

