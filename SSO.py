import os
import pyautogui
import time
import getpass
from sys import platform as _platform

credentialfile = '/tmp/pytest.txt'
usernamefield = (746, 135)
passwordfield = (930, 136)
loginbutton = (1104, 135)

def Detect(): # shit om platform te detecteren
    if _platform == "linux" or _platform == "linux2":
        print 'linux' # linux
    elif _platform == "darwin":
        print 'darwin' # MacOS
    elif _platform == "win32":
        print 'win32' # Windows
    elif _platform == "win64":
        print 'win64' # Windows 64-bit

def Save_Credentials(): #Saves username + password in txt file
    file = open('/tmp/pytest.txt', "r+",)
    new_username = input("Enter Username: ")
    file.write(new_username + ",")
    file.flush()

    pswd = getpass.getpass('Password:')
    new_password = pswd
    file.write(new_password)
    file.flush()
    Enter_Credentials()

def Enter_Credentials(): #enters credentials from txt files, logs in
    with open (credentialfile) as credentials: #open txt file with credentials
        for line in credentials:
            username = (line.split(',')[0]) #grabs username from file
            password = (line.split(',')[1]) #grabs password from file

    pyautogui.moveTo (usernamefield) #Select username field, enter username
    pyautogui.click()
    pyautogui.typewrite(username)
    time.sleep(0.5)

    pyautogui.moveTo (passwordfield) #Select username field, enter password
    pyautogui.click()
    pyautogui.typewrite(password)
    time.sleep(0.5)

    pyautogui.moveTo (loginbutton) # click login button
    #pyautogui.click()

def Login():
    if os.stat(credentialfile).st_size == 0: # If no credentials in txt run Save_Credentials()
        Save_Credentials()
    else:                              # else run Enter_Credentials()
        Enter_Credentials()

Login ()
