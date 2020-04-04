from tkinter import *
import tkinter.font as tkfont
import gui

route_no = ['1 SPL', 'C6Exp']
t4 = Tk()
t4.title('Choose the route number')
f = tkfont.Font(family='Sans Serif', size=12)
v3 = StringVar(t4)
v3.set(route_no[0])
w3 = OptionMenu(t4, v3, *route_no)
w3.config(bg='red3', fg='white', font=f)
w3.grid(row=1, column=0, padx=120, pady=30)
b = Button(t4, text='Proceed', bg='red3', fg='white', font=f, command=lambda: [gui.form(v3.get())])
b.grid(row=2, column=0, padx=120, pady=30)
t4.mainloop()
