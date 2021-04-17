import pyautogui, time
time.sleep(10)
f = open('filename', 'r')
for word in f:
  pyautogui.typewrite(word)
  pyautogui.press('Enter')
  #time.sleep(1.5)
