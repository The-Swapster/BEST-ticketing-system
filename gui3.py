from tkinter import *
import database as db



def show_entry_fields(v1, v2, a):
    t3 = Tk()
    t3.title("Ticket details")
    s = ''
    for i in range(a):
        l = db.data_entries_passenger(v1, v2)
        a = "Select * from passenger where ticket_id = ?"
        db.c.execute(a, (l,))
        r = db.c.fetchone()
        s += "Bus Number:" + str(r[0]) + "\nRoute Number: " + str(r[1]) + "\nTicket Id :" + str(
            r[2]) + "\nStart Stop: " + str(r[3]) + "\nEnd Stop: " + str(r[4]) + "\nType: " + str(r[5]) + "\n\n"
        print(s)
    l1 = Label(t3, text=s)
    l1.grid(row=0, column=0)
    #t3.mainloop()