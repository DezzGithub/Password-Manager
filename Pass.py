import sqlite3, hashlib
from tkinter import *

echo "# Passwordmanager" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/DezzGithub/Passwordmanager.git
git push -u origin main

window = Tk()

window.title("Passwortmanager")

def loginflaeche():
    window.geometry("250x100")

    lbl = Label(window,text="Passwort Eingeben")
    lbl.config(anchor=CENTER)
    lbl.pack()

    lbl1 = Label(window)
    lbl1.pack()


    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    def checkPassword():
        password = "test"
        if password == txt.get():
            print("Richtiges Passwort")
        else:
            lbl1.config(text="Falsches Passwort")

    

    btn = Button(window, text="Bestätigen", command=checkPassword)
    btn.pack(pady=10)

loginflaeche()
window.mainloop()