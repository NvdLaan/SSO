#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def new_app():
    win = tk.Toplevel()
    win.wm_title("New application")

    name1 = tk.Label(win, text="Name:")
    name1.grid(row=0, column=0)

    name2 = tk.Entry(win,)
    name2.grid(row=0, column=1)

    url1 = tk.Label(win, text="URL:")
    url1.grid(row=1, column=0)

    uname2 = tk.Entry(win,)
    uname2.grid(row=1, column=1)

    uname1 = tk.Label(win, text="Username:")
    uname1.grid(row=2, column=0)

    uname2 = tk.Entry(win,)
    uname2.grid(row=2, column=1)

    pass1 = tk.Label(win, text="Password:")
    pass1.grid(row=3, column=0)

    pass2 = tk.Entry(win, show='*')
    pass2.grid(row=3, column=1)

    butt1 = ttk.Button(win, text="Done!", command=win.destroy)
    butt1.grid(row=4, column=0)

    butt2 = ttk.Button(win, text="Cancel", command=win.destroy)
    butt2.grid(row=4, column=1)

def popup_showinfo():
    showinfo("Window", "Hello World!")

class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()

        self.greet_button = ttk.Button(self, text="New application", command=new_app) # Nieuwe applicatie knop
        self.greet_button.pack()

        self.button_showinfo = ttk.Button(self, text="Show Info", command=popup_showinfo)
        self.button_showinfo.pack()

root = tk.Tk()

app = Application(root)

root.mainloop()
