from asyncore import loop
from tkinter import  N
from pyautogui import*
import time
import keyboard
import random
import win32

time.sleep(1)

n = 60
b = 0

if n >= 60:
    a = "Minuten" 
    b = n/60
else:
    a = "Sekunde"


wiederholen = 1
while wiederholen < n + 1:
    print(wiederholen)
    time.sleep(1)
    wiederholen = wiederholen + 1
if n >= 60:
    print("Du hast", b, a, "deiner Zeit verschwändet")
else:
    print("Du hast", n, a, "deiner Zeit verschwändet") 