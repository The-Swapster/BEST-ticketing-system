from tkinter import *
import database as db
import random
from datetime import datetime

def bus_number(v):
    n = datetime.now()
    c = n.strftime("%H")
    if v == '1 SPL':
        if int(c) <= 11:
            return "MH01CD1234"
        elif 11 <= int(c) <= 13:
            return "MH01XY6754"
        elif 13 <= int(c) <= 15:
            return "MH01MD3245"
        elif 15 <= int(c) <= 18:
            return "MH01AB3848"
        else:
            return "MH01BA5705"
    elif v == 'C6Exp':
        if int(c) <= 11:
            return "MH01RM5018"
        elif 11 <= int(c) <= 13:
            return "MH01UA6550"
        elif 13 <= int(c) <= 15:
            return "MH01SA7745"
        elif 15 <= int(c) <= 18:
            return "MH01ZM8199"
        else:
            return "MH01DG1860"


def show_entry_fields(v1, v2, a, v):
    j = random.randint(100, 1000)
    t3 = Tk()
    t3.title("Ticket details")
    s = ''
    d = bus_number(v)
    #print(v1, v2, a, v)
    #for i in range(int(a)):
    j += 1
    #l = db.data_entries_passenger(v1, v2)
    #print(v1, v2, a)"
    db.c.execute('Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number) Values(?,?,?,?,?,?)', (d, v, v1, v2, j, a))
    db.connection.commit()
    #a = "Select * from passenger where ticket_id = ?"
    #db.c.execute(a, (i,))
    #r = db.c.fetchone()
    #s += "Bus Number:" + str(r[0]) + "\nRoute Number: " + str(r[1]) + "\nTicket Id :" + str(
        #r[2]) + "\nStart Stop: " + str(r[3]) + "\nEnd Stop: " + str(r[4]) + "\nType: " + str(r[5]) + "\n\n"
    #print(s)
    s += "Bus Number: " + str(d) + "\nRoute Number: " + str(v) + "\nTicket Id: "+ str(j) + "\nStart Stop: "+str(v1)+"\nEnd Stop: "+str(v2)+"\nNumber: "+str(a)+"\n\n"
    l1 = Label(t3, text=s)
    l1.grid(row=0, column=0)
    b1 = Button(t3, text='Close', command=t3.destroy)
    b1.grid(row=1)
    #t3.mainloop()
