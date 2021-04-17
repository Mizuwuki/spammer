import pyautogui, time
time.sleep(20)
f = open('filename', 'r')
for word in f:
  pyautogui.typewrite(word)
  pyautogui.press('Enter')
