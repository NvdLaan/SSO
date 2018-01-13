from tkinter import Tk, Label, Button
import time
import pyautogui
import os
import subprocess


def Open_Facebook():     
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://www.facebook.com/"])
def Open_Google():     
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://www.google.com/"])
def Open_Twitter():     
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://www.twitter.com/"])

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("SSO GUI")
        master.minsize(width=400, height=200)
        self.label = Label(master, text="Alle apps")
        self.label.pack()

        self.greet_button = Button(master, text="Facebook", command=self.Facebook)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Google", command=self.Google)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Twitter", command=self.Twitter)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def Facebook(self):
        Open_Facebook()
    def Google(self):
        Open_Google()
    def Twitter(self):
        Open_Twitter()


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
