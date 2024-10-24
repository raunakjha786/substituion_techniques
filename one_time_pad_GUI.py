import onetimepad
from tkinter import *
import tkinter as tk
class Onetime:
    def __init__(self, root):
        root.title("One-Time Pad-> Anon")
        self.label1 = Label(root, text='plain text')
        self.label1.grid(row=10, column=1)
        self.label2 = Label(root, text='encrypted text')
        self.label2.grid(row=11, column=1)
        self.l3 = Label(root, text="cipher text")
        self.l3.grid(row=10, column=10)
        self.l4 = Label(root, text="decrypted text")
        self.l4.grid(row=11, column=10)
        self.e1 = Entry(root)
        self.e1.grid(row=10, column=2)
        self.e2 = Entry(root)
        self.e2.grid(row=11, column=2)
        self.e3 = Entry(root)
        self.e3.grid(row=10, column=11)
        self.e4 = Entry(root)
        self.e4.grid(row=11, column=11)
        self.ent = Button(root, text="encrypt", bg="red", fg="white", command=self.encryptMessage)
        self.ent.grid(row=13, column=2)
        self.b2 = Button(root, text="decrypt", bg="green", fg="white", command=self.decryptMessage)
        self.b2.grid(row=13, column=11)
    def encryptMessage(self):
        pt = self.e1.get()
        ct = onetimepad.encrypt(pt, 'random')
        self.e2.insert(0, ct)
    def decryptMessage(self):
        ct1 = self.e3.get()
        pt1 = onetimepad.decrypt(ct1, 'random')
        self.e4.insert(0, pt1)
def build():
    root = tk.Tk()
    root.geometry("600x100")
    hc = Onetime(root)
    root.mainloop()