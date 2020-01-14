import os,time
import pyautogui as pag

old = (0, 0)
new = (0, 0)
try:
    while True:
        new = pag.position() #返回鼠标的坐标
        if (new != old):
            print(time.asctime( time.localtime(time.time()) )+ ' '+str(new))
        old = new
        time.sleep(1)
except  KeyboardInterrupt:
    print ('end....')