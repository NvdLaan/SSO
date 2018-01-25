#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def new_app():
    top = tk.Toplevel()
    top.wm_title("New application")

    name1 = tk.Label(top, text="Name:")
    name1.grid(row=0, column=0)

    name2 = tk.Entry(top,)
    name2.grid(row=0, column=1)
    name2.insert(0, "Facebook")

    url1 = tk.Label(top, text="URL:")
    url1.grid(row=1, column=0)

    uname2 = tk.Entry(top,)
    uname2.grid(row=1, column=1)
    uname = uname2.get()

    uname1 = tk.Label(top, text="Username:")
    uname1.grid(row=2, column=0)

    uname2 = tk.Entry(top,)
    uname2.grid(row=2, column=1)

    pass1 = tk.Label(top, text="Password:")
    pass1.grid(row=3, column=0)

    pass2 = tk.Entry(top, show='*')
    pass2.grid(row=3, column=1)

    butt1 = ttk.Button(top, text="Done!", command=top.destroy)
    butt1.grid(row=4, column=0)

    butt2 = ttk.Button(top, text="Cancel", command=top.destroy)
    butt2.grid(row=4, column=1)

def popup_showinfo():
    showinfo("Window", "Hello World!")

def popup_delete():
    top = tk.Toplevel()
    top.wm_title("Deletion...")

    msg1 = tk.Label(top, text="Do you really want to delete? No recovery possible!!")
    msg1.grid(row=0, column=0)

    butt1 = tk.Button(top, text="No", command=top.destroy) # exit window command
    butt1.grid(row=1, column=0)

    butt2 = tk.Button(top, text="Yes", command=top.destroy) # becomes delete command
    butt2.grid(row=1, column=1)


class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

        self.greet_button = ttk.Button(self, text="New application", command=new_app) # Nieuwe applicatie knop
        self.greet_button.pack()

        self.button_showinfo = ttk.Button(self, text="Show Info", command=popup_showinfo)
        self.button_showinfo.pack()

        self.button_showinfo = ttk.Button(self, text="Delete", command=popup_delete)
        self.button_showinfo.pack()

root = tk.Tk()

app = Application(root)

root.mainloop()
