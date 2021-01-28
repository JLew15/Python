import tkinter as tk
from tkinter import *

root = Tk()
root.title("Sample Survey")
root.geometry("720x485")
root.attributes("-fullscreen", False)

n = StringVar()

months = ('January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December',)

lbox = Listbox(root, listvariable=n, selectmode=MULTIPLE)

for month in months:
    lbox.insert("end", month)

lbox.grid()

root.mainloop()
