import pyautogui
script = "test test test test test test"

for x in script.split():
    pyautogui.write(x)
    pyautogui.press("enter")