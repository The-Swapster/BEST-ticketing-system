from tkinter import *
import tkinter.font as tkfont
import gui3
import webbrowser


def open(url):
    webbrowser.open_new(url)

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
    t1 = Toplevel()
    t1.title("Enter Ticket Details")
    f = tkfont.Font(family='Sans Serif', size=12)
    img = PhotoImage(file='best_1.png')
    b3 = Button(t1, image=img, command=lambda: open("https://www.bestundertaking.com/in/iis6954.asp?lang=en"))
    Button.image = img
    b3.grid(row=0)
    if v == '1 SPL':
        counter = IntVar(t1)
        variable = StringVar(t1)
        variable.set(Spl1[0])
        variable1 = StringVar(t1)
        variable1.set(Spl1[0])
        text3 = Label(t1, text="Source", font=f, bg='red3', fg='white')
        text4 = Label(t1, text="Destination", font=f, bg='red3', fg='white')
        text5 = Label(t1, text="Number of people", font=f, bg='red3', fg='white')
        w = OptionMenu(t1, variable, *Spl1)
        w.config(font=f, bg='red3', fg='white')
        w.grid(row=1, column=3, columnspan=3, padx=30)
        x = OptionMenu(t1, variable1, *Spl1)
        x.config(font=f, bg='red3', fg='white')
        x.grid(row=2, column=3, columnspan=3, padx=30)
        text3.grid(row=1, column=1, ipadx=48, padx=30, pady=30)
        text4.grid(row=2, column=1, ipadx=30, padx=30, pady=30)
        text5.grid(row=3, column=1, padx=30, pady=30)
        Label(t1, font=f, bg='red3', fg='white', textvariable=counter).grid(row=3, column=4, ipadx=70)
        Button(t1, text="+", font=f, bg='red3', fg='white', command=lambda: counter.set(counter.get() + 1)).grid(row=3, column=5)
        Button(t1, text="-", font=f, bg='red3', fg='white', command=lambda: counter.set(counter.get() - 1)).grid(row=3, column=3)
        button1 = Button(t1, text='Generate Ticket', font=f, bg='red3', fg='white',
                         command=lambda: [gui3.show_entry_fields(variable.get(), variable1.get(), counter.get(), v), t1.destroy()])
        button1.grid(row=9, column=2, pady=30)
    elif v == 'C6Exp':
        counter = IntVar(t1)
        variable = StringVar(t1)
        variable.set(C6Exp[0])
        variable1 = StringVar(t1)
        variable1.set(C6Exp[0])
        text3 = Label(t1, font=f, bg='red3', fg='white', text="Source")
        text4 = Label(t1, font=f, bg='red3', fg='white', text="Destination")
        text5 = Label(t1, font=f, bg='red3', fg='white', text="Number of people")
        w = OptionMenu(t1, variable, *C6Exp)
        w.config(font=f, bg='red3', fg='white')
        w.grid(row=1, column=3, columnspan=3, padx=30)
        x = OptionMenu(t1, variable1, *C6Exp)
        x.config(font=f, bg='red3', fg='white')
        x.grid(row=2, column=3, columnspan=3, padx=30)
        text3.grid(row=1, column=1, ipadx=48, padx=30, pady=30)
        text4.grid(row=2, column=1, ipadx=30, padx=30, pady=30)
        text5.grid(row=3, column=1, padx=30, pady=30)
        Label(t1, font=f, bg='red3', fg='white', text="Number of people").grid(row=3, column=1)
        Label(t1, font=f, bg='red3', fg='white', textvariable=counter).grid(row=3, column=4, ipadx=70)
        Button(t1, text="+", font=f, bg='red3', fg='white', command=lambda: counter.set(counter.get() + 1)).grid(row=3, column=5)
        Button(t1, text="-", font=f, bg='red3', fg='white', command=lambda: counter.set(counter.get() - 1)).grid(row=3, column=3)
        button1 = Button(t1, text='Generate Ticket', font=f, bg='red3', fg='white',
                         command=lambda: [gui3.show_entry_fields(variable.get(), variable1.get(), counter.get(), v), t1.destroy()])
        button1.grid(row=9, column=2, ipadx=48, pady=30)



