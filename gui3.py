from tkinter import *
import database as db
import random
from datetime import datetime
import sqlite3
import tkinter.font as tkfont

spl1 = {
    "Mumbai CST": 0,
    "Hutatma Chowk": 2,
    "Ahilyabai Holkar Chowk": 3,
    "Mantralay": 4.9,
    "NCPA": 5.6
}

C6Exp = {
    "Mumbai CST": 0,
    "Hutatma Chowk": 2,
    "Ahilyabai Holkar Chowk": 3,
    "Mantralay": 4.9,
    "NCPA": 5.6,
    "Colaba": 8.8,
    "Dr S P Mukherji Chowk Museum": 9.8,
    "Lions Gate": 10.05,
    "Old Custom House": 10.4,
    "RBI Fort": 10.85,
    "Swami D Saraswati Chowk Fort": 11.13,
    "Carnac Bander": 12.93,
    "Wadi Bander": 13.88,
    "Jijamata Nagar": 19.88,
    "Acharya Vidyaniketan": 30.88,
    "H P Nagar": 31.09,
    "Bpcl Sports Club Mahul": 31.38,
    "Shankar Mandir": 34.88,
    "Vashi Naka": 37.78,
    "Aziz Baug": 38.43,
    "Marawali Baug": 38.93,
    "Chembur Colony": 39.53,
    "Navjeevan Society (Chembur)": 39.88,
    "Basant Park": 40.18,
    "Chembur Naka Swami Vivekanand Chowk": 41.28,
    "Sandu Wadi": 42.78,
    "Acharya Gardendiamond Garden": 43.43,
    "10th Road Chembur Church": 44.28,
    "Dr. Ambedkar Garden": 45.68
}


def price(v, a, v1, v2):
    if v == '1 SPL':
        d = spl1[v2] - spl1[v1]
    elif v == 'C6Exp':
        d = C6Exp[v2] - C6Exp[v1]
    if d < 5:
        return a * 5
    elif 5 <= d < 10:
        return a * 10
    elif 10 <= d < 15:
        return a * 15
    else:
        return a * 20


def bus_number(v, a, v1, v2, p):
    j = random.randint(100, 1000)
    n = datetime.now()
    h = n.strftime("%H")
    s = ''
    if v == '1 SPL':
        if int(h) <= 11:
            db.c.execute("select count from passenger_count where bus_number = 'MH01CD1234'")
            count = db.c.fetchone()
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01CD1234', a))
                    db.connection.commit()
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01CD1234'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, price) Values(?,?,?,?,?,?,?)',
                    ('MH01CD1234', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01CD1234' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s

        elif 11 <= int(h) <= 13:
            db.c.execute("select count from passenger_count where bus_number = 'MH01XY6754'")
            count = db.c.fetchone()
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01XY6754', a))
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01XY6754'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, '
                    'price) Values(?,?,?,?,?,?,?)',
                    ('MH01XY6754', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01XY6754' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s

        elif 13 <= int(h) <= 15:
            db.c.execute("select count from passenger_count where bus_number = 'MH01MD3245'")
            count = db.c.fetchone()
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01MD3245', a))
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01MD3245'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, '
                    'price) Values(?,?,?,?,?,?,?)',
                    ('MH01MD3245', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01MD3245' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s

        elif 15 <= int(h) <= 18:
            db.c.execute("select count from passenger_count where bus_number = 'MH01AB3848'")
            count = db.c.fetchone()
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01AB3848', a))
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01AB3848'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, '
                    'price) Values(?,?,?,?,?,?,?)',
                    ('MH01AB3848', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01AB3848' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s

        else:
            db.c.execute("select count from passenger_count where bus_number = 'MH01BA5707'")
            count = db.c.fetchone()
            print(count)
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01BA5705', a))
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01BA5707'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, '
                    'price) Values(?,?,?,?,?,?,?)',
                    ('MH01BA5707', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01BA5707' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s

    elif v == 'C6Exp':
        if int(h) <= 11:
            db.c.execute("select count from passenger_count where bus_number = 'MH01RM5018'")
            count = db.c.fetchone()
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01RM5018', a))
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01RM5018'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, '
                    'price) Values(?,?,?,?,?,?,?)',
                    ('MH01RM5018', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01RM5018' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s

        elif 11 <= int(h) <= 13:
            db.c.execute("select count from passenger_count where bus_number = 'MH01UA6550'")
            count = db.c.fetchone()
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01UA6550', a))
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01UA6550'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, '
                    'price) Values(?,?,?,?,?,?,?)',
                    ('MH01UA6550', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01UA6550' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s

        elif 13 <= int(h) <= 15:
            db.c.execute("select count from passenger_count where bus_number = 'MH01SA7745'")
            count = db.c.fetchone()
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01SA7745', a))
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01SA7745'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, '
                    'price) Values(?,?,?,?,?,?,?)',
                    ('MH01SA7745', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01SA7745' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s

        elif 15 <= int(h) <= 18:
            db.c.execute("select count from passenger_count where bus_number = 'MH01ZM8199'")
            count = db.c.fetchone()
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01ZM8199', a))
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01ZM8199'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, '
                    'price) Values(?,?,?,?,?,?,?)',
                    ('MH01ZM8199', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01ZM8199' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s

        else:
            db.c.execute("select count from passenger_count where bus_number = 'MH01DG1860'")
            count = db.c.fetchone()
            if int(count[0]) <= 70:
                try:
                    db.c.execute("insert into passenger_count values(?,?)", ('MH01DG1860', a))
                except sqlite3.IntegrityError:
                    db.c.execute("update passenger_count set count = ? where bus_number = 'MH01DG1860'",
                                 (count[0] + a,))
                j += 1
                db.c.execute(
                    'Insert into passenger(bus_number, route_number, ticket_id, start_stop, end_stop, number, '
                    'price) Values(?,?,?,?,?,?,?)',
                    ('MH01DG1860', v, j, v1, v2, a, p))
                db.connection.commit()
                s += "Bus Number: " + 'MH01DG1860' + "\nRoute Number: " + str(v) + "\nTicket Id: " + str(
                    j) + "\nStart Stop: " + str(v1) + "\nEnd Stop: " + str(v2) + "\nNumber: " + str(
                    a) + "\nPrice: " + str(p) + "\n\n "
                return s
            else:
                s += 'Bus is full'
                return s


def show_entry_fields(v1, v2, a, v):
    t3 = Tk()
    t3.title("Ticket details")
    f = tkfont.Font(family='Consolas', size=12)
    p = price(v, a, v1, v2)
    s = bus_number(v, a, v1, v2, p)
    l1 = Label(t3, text=s, font=f)
    l1.grid(row=0, column=0)


