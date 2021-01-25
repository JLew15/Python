# Simple GUI
# Demonstrates creating a window.
from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title("My First GUI")
root.geometry("720x700")
root.attributes("-fullscreen", False)
root.bind("z", quit)


app = Frame(root)
app.grid()

myFont = tkFont.Font(family="Comic Sans MS", size=20)
lbl = Label(app, text="This is a label.", bg="cornflowerblue", fg="black", font=myFont)
lbl.grid()

button1 = Button(app, text="Don't click on me...", font=myFont, bg="cornflowerblue", fg="black")
button1.grid()
button2 = Button(app, text="Which one to click...", font=myFont, bg="cornflowerblue", fg="black")
button2.grid()


for i in range(5):
    x = Button(app)
    x["text"] = "This is button number " + str(i+1)
    x["font"] = myFont
    x["bg"] = "cornflowerblue"
    x["fg"] = "lime"
    x.grid()

# kick off the window's event loop
root.mainloop()