
   
import sqlite3, hashlib
from sqlite3.dbapi2 import Cursor
from tkinter import *

#Database Code
with sqlite3.connect("password_vault.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
id INTEGER PRIMARY KEY,
password TEXT NOT NULL);
""")

#Initiate Window
window = Tk()

window.title("Passwortmanager")

def hashPassword(input):
    hash = hashlib.md5(input)
    hash = hash.hexdigest()

    return hash

def firstScreen():
    window.geometry("250x150")

    lbl = Label(window, text="Passwort Erstellen")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Passwort erneut eingeben")
    lbl1.pack()


    txt1 = Entry(window, width=20, show="*")
    txt1.pack()
    txt1.focus()

    lbl2 = Label(window)
    lbl2.pack()

    def savePassword():
        if txt.get() == txt1.get():
            hashedPassword = hashPassword(txt.get().encode('utf-8'))

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?) """
            cursor.execute(insert_password, [(hashedPassword)])
            db.commit()

            passwordVault()
        else:
            lbl2.config(text="Password stimmt nicht überein")


    btn = Button(window, text="Speichern", command=savePassword)
    btn.pack(pady=10)


def loginflaeche():
    window.geometry("250x100")

    lbl = Label(window,text="Passwort Eingeben")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def getMasterPassword():
        checkHashedPassword = hashPassword(txt.get().encode('utf-8'))
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(checkHashedPassword)])

        return cursor.fetchall()

    def checkPassword():
        match = getMasterPassword()

        if match:
            passwordVault()
        else:
            txt.delete(0, 'end')
            lbl1.config(text="Falsches Passwort")

    btn = Button(window, text="Bestätigen", command=checkPassword)
    btn.pack(pady=10)

def passwordVault():
    for widget in window.winfo_children():
        widget.destroy()
    window.geometry("700x350")

    lbl = Label(window, text="Passwort Verwahrung")
    lbl.config(anchor=CENTER)
    lbl.pack()




cursor.execute("SELECT * FROM masterpassword")
if cursor.fetchall():
    loginflaeche()
else:
    firstScreen()


window.mainloop()
