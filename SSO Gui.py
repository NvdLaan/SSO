import os
import pyautogui
import time
import getpass
import base64
from sys import platform as _platform
from tkinter import Tk, Label, Button
import os
import subprocess
import webbrowser

file = 'c:\\temp\\applications.txt'


def create_file():
    file = open(filepath, "w+",)
    file.write("")
    file.flush()

def Save_Application():  # Saves username + password + version in txt file
    filepath = open(file,'a+')
    new_app = input("Voer applicatie naam in: ")
    filepath.write(new_app + "\n")
    filepath.flush()
    print("Nieuwe app is toegevoegd! Herstart om de nieuwe applicatie te gebruiken.")
   

class SSO_App:
    def __init__(self, master):
        self.master = master
        master.title("SSO GUI")
        master.minsize(width=400, height=200)
        self.label = Label(master, text="Alle apps")
        self.label.pack()

        
        self.greet_button = Button(master, text="New application", command=self.New_App)
        self.greet_button.pack()

        with open(file) as apps:
           for app in apps:
               self.greet_button = Button(master, text= app, command=lambda app = app:self.Run(app))
               self.greet_button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
               
    def Run(self, app):
        print ("SSO script voor de app", app)
        
    def New_App(self):
        Save_Application()
       

root = Tk()
SSO_App(root)
root.mainloop()
