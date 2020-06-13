import pyautogui
import time
import random
import sys
width,height =pyautogui.size()
counter=0
tim=4
moves=3

try:
              while True:
                            wi=random.randint(50,width-50)
                            hi=random.randint(50,height-50)
                            pyautogui.moveTo(wi,hi,duration=0.4)
                            counter+=1
                            if counter%moves == 0:
                                          temp=random.randint(0,tim)
                                          time.sleep(temp)
                                          
except KeyboardInterrupt:
              print("Exec Terminated.")
              sys.exit(0)
                            
