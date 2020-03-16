import tkinter as tk
import database_1 as db
import sqlite3

root = tk.Tk()
root.geometry("325x200")
root.title("Choose Bus")
counter=tk.IntVar()
list1 =[
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
variable = tk.StringVar(root)
variable.set(list1[0])
variable1 = tk.StringVar(root)
variable1.set(list1[0])

def show_entry_fields():
    t = tk.Tk()
    t.title("Ticket details")
    s=''
    a=counter.get()
    for i in range(a):
        l=db.data_entries_passenger(variable.get(),variable1.get())
        a = "Select * from passenger where ticket_id = ?"
        db.c.execute(a,(l,))
        r = db.c.fetchone()
        s += "Bus Number:"+ str(r[0])+ "\nRoute Number: "+ str(r[1])+ "\nTicket Id :"+ str(r[2])+ "\nStart Stop: "+ str(r[3])+ "\nEnd Stop: "+str(r[4])+ "\nType: "+str(r[5])+"\n\n"
    tk.Label(t, text=s).grid(row=0, column=0)
    t.mainloop()

button1 = tk.Button(text='Submit', command=show_entry_fields)
button1.grid(row=8, column=1, pady=4)
text3 = tk.Label(root, text="Source")
text4 = tk.Label(root, text="Destination")
text5 = tk.Label(root, text="Number of people")
w = tk.OptionMenu(root, variable, *list1)
w.grid(row=0, column=4)
x = tk.OptionMenu(root, variable1, *list1)
x.grid(row=1, column=4)
text3.grid(row=0, column=0)
text4.grid(row=1, column=0)
text5.grid(row=2, column=0)
tk.Label(root, text="Number of people").grid(row=2, column=0)
tk.Label(root, textvariable=counter).grid(row=2, column=5)
tk.Button(root, text="+", command=lambda: counter.set(counter.get()+1)).grid(row=2,column=6)
tk.Button(root, text="-", command=lambda: counter.set(counter.get()-1)).grid(row=2,column=4)
root.mainloop()

