import pyautogui

while True:
    #if mouse.is_pressed(button='left'):
    user_input = input("Press enter to print mouse location:")
    if user_input == (''):
        print(pyautogui.position())
        break
    else:
        pass
