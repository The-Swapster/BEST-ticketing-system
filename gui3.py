from tkinter import *
import database as db
import random


def show_entry_fields(v1, v2, a):
    j = random.randint(100, 1000)
    t3 = Tk()
    t3.title("Ticket details")
    s = ''
    print(v1, v2, a)
    #for i in range(int(a)):
    j += 1
    #l = db.data_entries_passenger(v1, v2)
    #print(v1, v2, a)"
    db.c.execute('Insert into passenger(ticket_id, start_stop, end_stop, number) Values(?,?,?,?)', (j, v1, v2, a))
    db.connection.commit()
    #a = "Select * from passenger where ticket_id = ?"
    #db.c.execute(a, (i,))
    #r = db.c.fetchone()
    #s += "Bus Number:" + str(r[0]) + "\nRoute Number: " + str(r[1]) + "\nTicket Id :" + str(
        #r[2]) + "\nStart Stop: " + str(r[3]) + "\nEnd Stop: " + str(r[4]) + "\nType: " + str(r[5]) + "\n\n"
    #print(s)
    s += "Bus Number: " + "\nRoute Number: " + "\nTicket Id: "+ str(j) + "\nStart Stop: "+str(v1)+"\nEnd Stop: "+str(v2)+"\nNumber: "+str(a)+"\n\n"
    l1 = Label(t3, text=s)
    l1.grid(row=0, column=0)
    #t3.mainloop()
