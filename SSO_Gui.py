#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

import os
import pyautogui
import time
import getpass
import base64
from sys import platform as _platform
import sys
from tkinter import Tk, Label, Button
import subprocess
import webbrowser


def Detect():  # Detect the platform
    if _platform == "linux" or _platform == "linux2":
        return 'linux'  # linux
    elif _platform == "darwin":
        return 'darwin'  # MacOS
    elif _platform == "win32":
        return 'win32'  # Windows
    elif _platform == "win64":
        return 'win64'  # Windows 64-bit
    else:
        print('Error: Platform unknown')

pf = Detect()  # Creates variable with output of Detect()

def Pathgen():
    if pf == "linux" or pf == "darwin":
        return '/tmp/SSO/'
    elif pf == "win32" or pf == "win64":
        return 'c:\\temp\\SSO\\'


app_path = Pathgen()
file = app_path + 'applications.txt'  #Lijst met applicaties

def Select():   # selects field and returns mouse location
    while True:
        user_input = input("Press enter to select:")
        if user_input == (''):
            field = (pyautogui.position())
            return field
            break


def New_Application():
    new_app_name = input("Voer applicatie naam in: ") # App name
    new_app_file = app_path + new_app_name + ".txt"   # config bestandje nieuwe app wordt aangemaakt
    new_file = open(new_app_file,"a+",)
    new_file.write(new_app_name + "\n")                  #appnaam wordt in bestandje geschreven
    new_file.write(input("Enter URL: https://")+ "\n")    #URL wordt in bestandje weggeschreven
    new_file.write(input("Enter Username: ")+ "\n")         #username
    new_file.write(getpass.getpass('Enter Password:')+ "\n")
    #pswd = getpass.getpass('Password:')       #password
    new_file.flush()

    new_file = open(new_app_file,"r+",)
    new_app_url = new_file.readlines()[1]
    new_app_url = new_app_url.strip("\n") #removes \n(whitespace) from txt
    webbrowser.open("https://" + new_app_url)    #opent ingevoerde url, "https://" heb ik ervoor gezet omdat windows IE opent zonder.

    print('Place your pointer on the usernamefield:')
    new_file = open(new_app_file,"a",)
    usernamefield = Select()
    new_file.write((str(usernamefield[0]))+"\n")
    new_file.write((str(usernamefield[1]))+"\n")


    print('Place your pointer on the passwordfield:')
    passwordfield = Select()
    new_file.write((str(passwordfield[0]))+"\n")
    new_file.write((str(passwordfield[1]))+"\n")

    print('Place your pointer on the login button:')
    loginbutton = Select()
    new_file.write((str(loginbutton[0]))+"\n" )
    new_file.write((str(loginbutton[1]))+"\n" )
    new_file.flush()

    new_file = open(file, "a")             # Nieuwe app wordt in applications.txt gezet zodat deze dichtbaar wordt in het menu.
    new_file.write (new_app_name + "\n")
    print("De nieuwe applicatie is toegevoegd! Herstart om de applicatie te kunnen gebruiken.") #herstart knop komt nog denk ik

class SSO_App:
    def __init__(self, master):
        self.master = master
        master.title("SSO GUI")
        master.minsize(width=400, height=200)
        self.label = Label(master, text="Alle apps")
        self.label.pack()


        self.greet_button = Button(master, text="New application", command=self.New_App) # Nieuwe applicatie knop
        self.greet_button.pack()

        with open(file) as apps:
           for app in apps:        #loopt door applications.txt, maakt knop van elke applicatie in de lijst
               app=app.strip("\n")
               self.greet_button = Button(master, text= app, command=lambda app = app:self.Run(app)) #opent de applicatie knop, geeft app name als variable(app) mee
               self.greet_button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def Run(self, app):
        app= app.strip("\n") #removes \n(whitespace) from txt
        with open(app_path + app + ".txt") as credentials:  # open txt file with credentials + settings
            credentials_list = []
            for line in credentials:
                line = line.strip("\n")
                credentials_list.append(line)           #gooit settings in credentials_list om variables te zetten.

            #Zet variables op basis van eerder gemaakte lijst van text bestand
            app_name = credentials_list[0]
            app_url = credentials_list[1]
            app_username = credentials_list[2]
            app_password = credentials_list[3]
            #zet coordinaten in variabeles, maakt er integers van.
            app_username_fieldx = int(credentials_list[4])
            app_username_fieldy = int(credentials_list[5])
            app_password_fieldx = int(credentials_list[6])
            app_password_fieldy = int(credentials_list[7])
            app_login_buttonx = int(credentials_list[8])
            app_login_buttony = int(credentials_list[9])

            # open webbrowser etc..
            webbrowser.open("https://" + app_url)
            time.sleep(3) #slakken stand

            pyautogui.moveTo(app_username_fieldx, app_username_fieldy)  # Select username field, enter username
            pyautogui.click(clicks=3)
            pyautogui.typewrite(app_username)


            pyautogui.moveTo(app_password_fieldx, app_password_fieldy)  # Select username field, enter password
            pyautogui.click(clicks=3)
            pyautogui.typewrite(app_password)


            pyautogui.moveTo(app_login_buttonx, app_login_buttony)  # click login button
            pyautogui.click()



    def New_App(self):
        New_Application()


root = Tk()
SSO_App(root)

root.mainloop()
