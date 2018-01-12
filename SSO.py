import os
import pyautogui
import time
import getpass
import base64
from sys import platform as _platform

### User configurable variables ###

# Filename in /tmp/ (MacOS & Linux) or c:\\temp\\ (Windows)
filename = 'pytest.db'

### END User configurable variables ###

version = '0.2.0' # Versioning to prevent file conflicts

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


filepath = Start()  # Creates filepath variable with output of  Start()

def Save_Credentials():  # Saves username + password + version in txt file
    file = open(filepath, "w+",)
    file.write(version + ";")
    new_username = input("Enter Username: ")
    file.write(new_username + ";")
    file.flush()

    pswd = getpass.getpass('Password:')
    # Creates a variable with the hidden password prompt
    new_password = base64.b64encode(pswd.encode())  # Encodes password
    file.write(new_password.decode('utf-8'))
    file.flush()
    print('Now select the username field in 10 seconds')
    time.sleep(5)
    print('5 Seconds')
    time.sleep(1)
    print('4 Seconds')
    time.sleep(1)
    print('3 Seconds')
    time.sleep(1)
    print('2 Seconds')
    time.sleep(1)
    print('1 Seconds')
    time.sleep(1)
    usernamefield = pyautogui.position()
    file.write(';' + (str(usernamefield)))
    file.flush()
    print(usernamefield)
    print('Now select the password field in 10 seconds')
    time.sleep(5)
    print('5 Seconds')
    time.sleep(1)
    print('4 Seconds')
    time.sleep(1)
    print('3 Seconds')
    time.sleep(1)
    print('2 Seconds')
    time.sleep(1)
    print('1 Seconds')
    time.sleep(1)
    passwordfield = pyautogui.position()
    file.write(';' + (str(passwordfield)))
    file.flush()
    print(passwordfield)
    print('Now select the button in 10 seconds')
    time.sleep(5)
    print('5 Seconds')
    time.sleep(1)
    print('4 Seconds')
    time.sleep(1)
    print('3 Seconds')
    time.sleep(1)
    print('2 Seconds')
    time.sleep(1)
    print('1 Seconds')
    time.sleep(1)
    loginbutton = pyautogui.position()
    file.write(';' + (str(loginbutton)))
    file.flush()
    print(loginbutton)
    Enter_Credentials()


def Enter_Credentials():  # enters credentials from txt files, logs in
    with open(filepath) as credentials:  # open txt file with credentials
        for line in credentials:

            username = (line.split(';')[1])  # grabs username from file
            encoded = (line.split(';')[2])  # grabs encoded password from file
            passwordRaw = base64.b64decode(encoded)  # Decodes password
            password = passwordRaw.decode("utf-8")
            readusernamefield = (line.split(';')[3])
            readpasswordfield = (line.split(';')[4])
            readloginbutton = (line.split(';')[5])

    pyautogui.moveTo(readusernamefield)  # Select username field, enter username
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    pyautogui.typewrite(username)
    time.sleep(0.5)

    pyautogui.moveTo(readpasswordfield)  # Select username field, enter password
    pyautogui.click()
    pyautogui.typewrite(password)
    time.sleep(0.5)

    pyautogui.moveTo(readloginbutton)  # click login button
    pyautogui.click()


def Version():
    with open(filepath) as credentials:  # open file with version
        for line in credentials:
            return (line.split(';')[0])


def Login(): # Perform various checks what to do
    if os.path.isfile(filepath):
        # If file exists run content check
        if os.stat(filepath).st_size == 0:
            # If file has no content run Save_Credentials()
            Save_Credentials()
        elif os.stat(filepath).st_size > 0:
            # If file has content and is the same version run Enter_Credentials()
            if version == (Version()):
                Enter_Credentials()
            else:
            # If version is incorrect prompt for user action
                print('Version is different!!')
                print('Do you want to rewrite the .db file?')
                answer = input('Please indicate approval: [y/n]')
                if not answer or answer[0].lower() != 'y':
                    print('You did not indicate approval')
                    exit(1)
                Save_Credentials()
    else:  # else run Save_Credentials()
        Save_Credentials()


Login()  # Run the Login() function
"""
with open(filepath) as credentials:  # open file with version
    for line in credentials:

        print(line.split(';')[0])
        print(line.split(';')[1])
        print(line.split(';')[2])
        print(line.split(';')[3])
        print(line.split(';')[4])
        print(line.split(';')[5])
"""
