import os
import pyautogui
import time
import getpass
import base64
from sys import platform as _platform

### User configurable variables ###

filename = 'pytest.db'
# Filename in /tmp/ (MacOS & Linux) or c:\\temp\\ (Windows)
usernamefield = (746, 135) # Respective GUI field location
passwordfield = (930, 136) # Respective GUI field location
loginbutton = (1104, 135) # Respective GUI button location

### END User configurable variables ###

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


def Start():  # Compares the platform variable to the respected platform...
    # and returns the path+filename
    if pf == "linux":
        return '/tmp/' + filename
    elif pf == "darwin":
        return '/tmp/' + filename
    elif pf == "win32":
        return 'c:\\temp\\' + filename
    elif pf == "win64":
        return 'c:\\temp\\' + filename


def Save_Credentials():  # Saves username + password in txt file
    file = open(filepath, "w+",)
    new_username = input("Enter Username: ")
    file.write(new_username + ",")
    file.flush()

    pswd = getpass.getpass('Password:')
    # Creates a variable with the hidden password prompt
    new_password = base64.b64encode(pswd.encode())  # Encodes password
    file.write(new_password.decode('utf-8'))
    file.flush()
    Enter_Credentials()


def Enter_Credentials():  # enters credentials from txt files, logs in
    with open(filepath) as credentials:  # open txt file with credentials
        for line in credentials:
            username = (line.split(',')[0])  # grabs username from file
            encoded = (line.split(',')[1])  # grabs encoded password from file
            passwordRaw = base64.b64decode(encoded)  # Decodes password
            password = passwordRaw.decode("utf-8")

    pyautogui.moveTo(usernamefield)  # Select username field, enter username
    pyautogui.click()
    pyautogui.typewrite(username)
    time.sleep(0.5)

    pyautogui.moveTo(passwordfield)  # Select username field, enter password
    pyautogui.click()
    pyautogui.typewrite(password)
    time.sleep(0.5)

    pyautogui.moveTo(loginbutton)  # click login button
    # pyautogui.click()


def Login(): # Perform various checks what to do
    if os.path.isfile(filepath):
        # If file exists run content check
        if os.stat(filepath).st_size == 0:
            # If file has no content run Save_Credentials()
            Save_Credentials()
        elif os.stat(filepath).st_size > 0:
            # If file has content run Enter_Credentials()
            Enter_Credentials()
    else:  # else run Save_Credentials()
        Save_Credentials()


filepath = Start()  # Creates filepath variable with output of  Start()
pf = Detect()  # Creates variable with output of Detect()

Login()  # Run the Login() function
