from tkinter import *
from tkinter import ttk
from tkinter import font
import calendar
import time
import datetime
import winsound

def gmtnow(alarm):
    """Getting Greenwich Mean Time. (Based on UNIX Epoch time.)"""

    seconds = calendar.timegm(time.gmtime())

    current_second = seconds % 60

    minutes = seconds // 60

    current_minute = minutes % 60

    hours = minutes // 60

    current_hour = hours % 24
    current_hour -= 6

    if current_hour >= 12:
        atag = "PM"
        current_hour -= 12
        if current_hour == 0:
            current_hour = 12
    else:
        atag = "AM"
        if current_hour == 0:
            current_hour = 12
    if current_hour < 10:
        adj_hour = "0"+str(current_hour)
    else:
        adj_hour = str(current_hour)
    if current_minute < 10:
        adj_minute = "0"+str(current_minute)
    else:
        adj_minute = str(current_minute)
    if current_second < 10:
        adj_second = "0"+str(current_second)
    else:
        adj_second = str(current_second)

    time_String = str.format("{:2}:{:2}:{:2}{}",adj_hour,adj_minute,adj_second,atag)

    if alarm == time_String:
        alarm_snd()

    return time_String

def show_time():
    time = gmtnow(alarm)
    txt.set(time)
    root.after(1000,show_time)

def alarm_snd():
    for i in range(5):
        winsound.Beep(750,1000)
        winsound.Beep(1000,1000)
        winsound.Beep(1250,1000)

def alarm_input():
    """GET ALARM TIME TO SET"""
    ahour = input("What hour?")
    aminute = input("What minute?")
    asecond = "00"
    atag = input("AM or PM".upper())
    if len(ahour) < 2:
        ahour = "0"+ahour
    if len(aminute)<2:
        aminute = "0"+aminute
    alarm = str.format("{:2}:{:2}:{:2}{}",ahour,aminute,asecond,atag)

    return alarm

alarm = alarm_input()
root = Tk()
root.geometry("800x200")
root.attributes("-fullscreen", False)
root.configure(background = "black")
root.bind("l", quit)
root.after(1000, show_time)
fnt = font.Font(family = "Century Gothic",size = 60, weight = "normal")
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font = fnt,background="black",foreground = "white")
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
