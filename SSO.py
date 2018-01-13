import os
import pyautogui
import time
import getpass
import base64
from sys import platform as _platform
from tkinter import Tk, Label, Button
import os
import subprocess



### User configurable variables ###

filename = 'pytest.db'
# Filename in /tmp/ (MacOS & Linux) or c:\\temp\\ (Windows)
usernamefield = (746, 135) # Respective GUI field location
passwordfield = (930, 136) # Respective GUI field location
loginbutton = (1104, 135) # Respective GUI button location

### END User configurable variables ###

version = '0.1.3' # Versioning to prevent file conflicts

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
    file.write(version + ",")
    new_username = input("Enter Username: ")
    file.write(new_username + ",")
    file.flush()

    pswd = getpass.getpass('Password:')
    # Creates a variable with the hidden password prompt
    new_password = base64.b64encode(pswd.encode())  # Encodes password
    file.write(new_password.decode('utf-8'))
    file.flush()
    Enter_Credentials()

#Open applicaties in chrome    
def Open_Facebook():     
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://www.facebook.com/"])
def Open_Google():     
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://www.google.com/"])
def Open_Twitter():     
    subprocess.Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://www.twitter.com/"])



def Enter_Credentials():  # enters credentials from txt files, logs in
    Open_Facebook()
    time.sleep(1)
    with open(filepath) as credentials:  # open txt file with credentials
        for line in credentials:

            username = (line.split(',')[1])  # grabs username from file
            encoded = (line.split(',')[2])  # grabs encoded password from file
            passwordRaw = base64.b64decode(encoded)  # Decodes password
            password = passwordRaw.decode("utf-8")

    pyautogui.moveTo(usernamefield)  # Select username field, enter username
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()
    pyautogui.typewrite(username)
    time.sleep(0.5)

    pyautogui.moveTo(passwordfield)  # Select username field, enter password
    pyautogui.click()
    pyautogui.typewrite(password)
    time.sleep(0.5)

    pyautogui.moveTo(loginbutton)  # click login button
    #pyautogui.click()


def Version():
    with open(filepath) as credentials:  # open file with version
        for line in credentials:
            return (line.split(',')[0])


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
       
class SSO_App:
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
        Login()
    def Google(self):
        Open_Google()
    def Twitter(self):
        Open_Twitter()


root = Tk()
my_gui = SSO_App(root)
root.mainloop()


# Login()  # Run the Login() function
