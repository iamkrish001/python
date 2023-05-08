import pyautogui 
import turtle
import time
name = input("What is your name?- ")
email = input("what is your email address?- ")
time.sleep(5)
pyautogui.click(1060,1048) #click chrome 
time.sleep(4) #wait 2 sec
pyautogui.click(1617,194) #click gmail
time.sleep(3) # wait 3 seconds
pyautogui.click(89,271) # click composePra
time.sleep(2) #wait 2 sec
pyautogui.moveTo(1573,466) #move to 'To' 
pyautogui.write(email) #write down the email address
pyautogui.click(1757,463)
pyautogui.write("Auto written mail")
pyautogui.click(1381,575)
pyautogui.write("Hey "+ name+" this is a automatic written mail using python. Have a great day :))")
pyautogui.click(1137,953)
