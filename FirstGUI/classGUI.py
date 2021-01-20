from tkinter import *

class Application(Frame):
    """A GUI app with three buttons"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.createWidgets()
        self.clicks = 0

    def createWidgets(self):
        self.totalLabel = Label(self, text="Total clicks")
        self.numClicks = Label(self, text=str(self.clicks))

        self.clickButton = Button(self, text="Click me.")
        self.antiButton = Button(self, text="Don't click me.")

        self.colorButton = Button(self, text="Change colors")

        self.totalLabel.grid()
        self.numClicks.grid()
        self.clickButton.grid()
        self.antiButton.grid()
        self.colorButton.grid()




root = Tk()
root.title("My First GUI")
root.geometry("720x700")
root.attributes("-fullscreen", False)
root.bind("z", quit)

root.mainloop()