import time, math
import pyautogui

time.sleep(15)
start_x = pyautogui.position()
start_y = pyautogui.position()

for a in range(0, 360, 10):
    start = start_x + int(200 * math.cos(math.radians(a)))
    stop = start_y + int(200 * math.sin(math.radians(a)))
     
    pyautogui.moveTo(start, stop, duration=0.3) 
    
    if a == 0:
        pyautogui.mouseDown(start=start_x, stop=start_y, button='left') 
        
    time.sleep(0.2) 
pyautogui.mouseUp(button='left')
