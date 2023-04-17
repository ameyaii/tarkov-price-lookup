from pyautogui import *
import keyboard
import pyautogui
import cv2 
import pytesseract
import requests
import json
from thefuzz import fuzz
from thefuzz import process
global item 
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\tesseract\\tesseract.exe'
noway= "<Response [200]>"
def smal():
    pic = pyautogui.screenshot(region=(x,y,300,22))
    pic.save(r'fun.png')
    img = cv2.imread('fun.png')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)  
    item = (pytesseract.image_to_string(img))
    print(item)
    comp = ""
    if item == comp:
        return
    else:
        pass
    item = item.split(remove, 1)[0]
    item = item.split(remove1, 1)[0]
    item = item.split(remove2, 1)[0]
    item = item.split(remove3, 1)[0]
    item = item.split(remove4, 1)[0]
    balls = requests.get('https://tarkov-market.com/api/v1/item?q={}&x-api-key='.format(item))
    item = balls.json()
    item = str(item)
    if "[]" in item:
        return
    else:
        pass
    item = (item.split(","))
    a,b,c = (item[6], item[10], item[11], )
    if "shortName" in a:
        a = item[7]
        c= item[12]
        b = item[11]
    else:
        pass
    a = a.split(":")
    c = c.split(":")
    b = b.split(":")
   
    print ("Flea price/Item Name", a[1])
    b =  (b[1])
    print ("Trader Price", c[1])
    b = b.replace("'",'')
    print (b)

    #file = open('message.txt', encoding="utf8")pi
    #if item == file.read():
    #    print('Success')
    #else:
    #    print('Fail')
remove = '|'
remove1 = '['
remove2 = '‘'
remove3 = '@'
remove4 = '‘'

while True:
    x, y = pyautogui.position()
    x = x + 9
    y = y - 33
    if keyboard.is_pressed('k'):
        smal()



