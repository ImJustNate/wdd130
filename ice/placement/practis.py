import pyautogui as pt
from time import sleep

sleep(2)
c = 5
rotations = 1
rotations += 1 
print ("down")
print (rotations)
while (c != 0):
    pt.keyDown('z')
    sleep(0.5)
    pt.keyUp('z')
    pt.keyUp('x')
    c -= 1
    print ('Time remaining=', c)