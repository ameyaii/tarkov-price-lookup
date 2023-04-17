import tkinter as tk
from ctypes import windll
import time
windll.shcore.SetProcessDpiAwareness(1)
price = 10023

root = tk.Tk()
root.title('Overlay')
root.wm_attributes("-topmost", True)
root.geometry('200x200+1600+100')
m = tk.Label(root, background='white', text= price)
root.attributes('-alpha', 0.5)
root.wm_attributes('-transparentcolor', 'white')
invis= tk.Frame(root, width=200, height=200, bg='white')
def update(txt):
    text1.configure(text=txt)

text1 = tk.Label(root, text='1')
text1.pack()
m.pack()
invis.pack()
root.mainloop()
while True:
    update('1')
    time.sleep(2.5)


