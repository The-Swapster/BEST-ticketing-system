import sqlite3
import random

id = random.randint(100, 1000)
connection = sqlite3.connect('BEST.db')
c = connection.cursor()


def create_table():
    c.execute(
        'create table if not exists bus(bus_number text primary key, route_number text, source text, destination '
        'text, seats real, standing_capacity real, driver_name text, conductor_name text)')
    c.execute(
        'create table if not exists seats(bus_number text, women_reserved real, handicaped_reserved real, '
        'senior_reserved real,others real, foreign key(bus_number) REFERENCES bus(bus_number))')
    c.execute(
        'create table if not exists bus_stop(name text , route_number text, constraint id primary key (name, '
        'route_number), foreign key(route_number) references bus(route_number))')
    c.execute(
        'create table if not exists passenger(bus_number text, route_number text, ticket_id real primary key, '
        'start_stop text, end_stop text, type text, foreign key(bus_number) references bus(bus_number), foreign key('
        'route_number) references bus(route_number))')
    c.execute(
        'create table if not exists bus_status(bus_number text unique, current_location text, passenger_count real, '
        'available_seats real, foreign key(bus_number) references bus(bus_number))')
    c.execute(
        'create table if not exists passenger_count(bus_number text, standing real, sitting real, foreign key('
        'bus_number) references bus(bus_number))')


def data_entries_bus():
    c.execute(
        "insert into bus values('MH01CD1234', '1SPL', 'Mumbai CSMT', 'NCPA', 51, 20, 'Vinayak Rao', 'Gaitonde Ganpat')")
    c.execute(
        "insert into bus values('MH01XY6754', '1SPL', 'Mumbai CSMT', 'NCPA', 51, 20, 'Mukund Narvekar', "
        "'Suhas Deshmukh')")
    c.execute(
        "insert into bus values('MH01MD3245', '1SPL', 'Mumbai CSMT', 'NCPA', 51, 20, 'Malhar Holkar', "
        "'Mahesh  Manjrekar')")
    c.execute(
        "insert into bus values('MH01AB3848', '1SPL', 'Mumbai CSMT', 'NCPA', 51, 20, 'Makrand Deshpande', "
        "'Keshav Tilak')")
    c.execute(
        "insert into bus values('MH01BA5705', '1SPL', 'Mumbai CSMT', 'NCPA', 51, 20, 'Upender Shukla', 'Gopal Gokhle')")
    c.execute(
        "insert into bus values('MH01RM5018', 'C6Exp', 'Colaba', 'Dr. Ambedkar Garden', 51, 20, 'Suresh Prabhu', "
        "'Dilip Kumar')")
    c.execute(
        "insert into bus values('MH01UA6550', 'C6Exp', 'Colaba', 'Dr. Ambedkar Garden', 51, 20, 'Mangesh Kale', "
        "'Manohar Parekar')")
    c.execute(
        "insert into bus values('MH01SA7745', 'C6Exp', 'Colaba', 'Dr. Ambedkar Garden', 51, 20, 'Lakshmikant Berede', "
        "'Umesh Wagmare')")
    c.execute(
        "insert into bus values('MH01ZM8199', 'C6Exp', 'Colaba', 'Dr. Ambedkar Garden', 51, 20, 'Ramakant Yadav', "
        "'Girish Kadam')")
    c.execute(
        "insert into bus values('MH01DG1860', 'C6Exp', 'Colaba', 'Dr. Ambedkar Garden', 51, 20, 'Subodh Deshpande', "
        "'Ashok Shroff')")


def data_entries_seats():
    c.execute("insert into seats values('MH01CD1234', 12, 3, 4, 32)")
    c.execute("insert into seats values('MH01XY6754', 12, 3, 4, 32)")
    c.execute("insert into seats values('MH01MD3245', 12, 3, 4, 32)")
    c.execute("insert into seats values('MH01AB3848', 12, 3, 4, 32)")
    c.execute("insert into seats values('MH01BA5707', 12, 3, 4, 32)")
    c.execute("insert into seats values('MH01RM5018', 12, 3, 4, 32)")
    c.execute("insert into seats values('MH01UA6550', 12, 3, 4, 32)")
    c.execute("insert into seats values('MH01SA7745', 12, 3, 4, 32)")
    c.execute("insert into seats values('MH01ZM8199', 12, 3, 4, 32)")
    c.execute("insert into seats values('MH01DG1860', 12, 3, 4, 32)")


def data_entries_bus_stop():
    c.execute("insert into bus_stop(name, route_number) values('Mumbai CST', '1SPL')")
    c.execute("insert into bus_stop(name, route_number) values('Hutatma Chowk', '1SPL')")
    c.execute("insert into bus_stop(name, route_number) values('Ahilyabai Holkar Chowk', '1SPL')")
    c.execute("insert into bus_stop(name, route_number) values('Mantralay', '1SPL')")
    c.execute("insert into bus_stop(name, route_number) values('NCPA', '1SPL')")
    c.execute("insert into bus_stop(name, route_number) values('Colaba', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Dr S P Mukherji Chowk Museum', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Lions Gate', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Old Custom House', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('RBI Fort', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Swami D Saraswati Chowk Fort', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Mumbai CST', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Carnac Bander', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Wadi Bander', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Jijamata Nagar', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Acharya Vidyaniketan', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('H P Nagar', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Bpcl Sports Club Mahul', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Shankar Mandir', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Vashi Naka', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Aziz Baug', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Marawali Baug', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Chembur Colony', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Navjeevan Society (Chembur)', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Basant Park', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Chembur Naka Swami Vivekanand Chowk', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Sandu Wadi', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Acharya Gardendiamond Garden', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('10th Road Chembur Church', 'C6Exp')")
    c.execute("insert into bus_stop(name, route_number) values('Dr. Ambedkar Garden', 'C6Exp')")
    #connection.commit()
    #c.close()
    #connection.close()

def data_entries_passenger(start, stop):
    id += 1
    c.execute("Insert into passenger(ticket_id,start_stop,end_stop) values(?,?,?)", (id, start, stop))
    #connection.commit()
    return id

def calls():
    create_table()
    data_entries_bus()
    data_entries_seats()
    data_entries_bus_stop()

