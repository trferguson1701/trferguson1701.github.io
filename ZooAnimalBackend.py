""" 
Backend aspect of program designed to 
implement functionality and data 
structures.

"""

import sqlite3

#Creation of connection to database

def connect():
    conn=sqlite3.connect("animals.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS animals (id INTEGER PRIMARY KEY, species text, name text, age text, feeding text)")
    conn.commit()
    conn.close()

#Insert functionality

def insert(species, name, age, feeding):
    conn=sqlite3.connect("animals.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO animals VALUES (NULL,?,?,?,?)",(species,name,age,feeding))
    conn.commit()
    conn.close()

#View Functionality

def view():
    conn=sqlite3.connect("animals.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM animals")
    rows=cur.fetchall()
    conn.close()
    return rows

#Serach Functionality

def search(species="", name="", age="", feeding=""):
    conn=sqlite3.connect("animals.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM animals WHERE species=? OR name=? OR age=? OR feeding=?", (species,name,age,feeding))
    rows=cur.fetchall()
    conn.close()
    return rows

#Delete Functionality

def delete(id):
    conn=sqlite3.connect("animals.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM animals WHERE id=?",(id,))
    conn.commit()
    conn.close()

#Update Functionality

def update(id,species,name,age,feeding):
    conn=sqlite3.connect("animals.db")
    cur=conn.cursor()
    cur.execute("UPDATE animals SET species=?, name=?, age=?, feeding=? WHERE id=?",(species,name,age,feeding,id))
    conn.commit()
    conn.close()




connect()


