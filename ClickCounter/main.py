from tkinter import *
import datetime


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.total = 0
        self.colors = ["#000000", "#FFFFFF", "#F00000", "#0F0000", "#00F000", "#000F00", "#0000F0", "#00000F"]
        self.colorIndex = 0
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self, text="Total People:")
        self.label2 = Label(self, text=str(self.total))
        self.buttonAdd = Button(self, text="+ Person")
        self.buttonAdd.config(command=self.addToCount)
        self.buttonRm = Button(self, text="- Person")
        self.buttonRm.config(command=self.rmFromCount)
        self.buttonColor = Button(self, text="Change Color", width=28, height=5)
        self.buttonColor.config(command=self.changeColor)

        self.label1.grid()
        self.label2.grid()
        self.buttonAdd.grid()
        self.buttonRm.grid()
        self.buttonColor.grid()

    def addToCount(self):
        self.total += 1
        if 10 > self.total > 0:
            self.label1.config(bg="green")
        elif 9 < self.total < 25:
            self.label1.config(bg="yellow")
        elif self.total > 25:
            self.label1.config(bg="red")
        print(self.total)
        self.label2.config(text=str(self.total))





    def rmFromCount(self):
        self.total -= 1
        if self.total < 0:
            self.label1.config(bg="pink")
        elif 10 > self.total > 0:
            self.label1.config(bg="green")
        elif 9 < self.total < 25:
            self.label1.config(bg="yellow")
        elif self.total > 25:
            self.label1.config(bg="red")
        print(self.total)
        self.label2.config(text=str(self.total))

    def changeColor(self):
        self.colorIndex += 1
        if self.colorIndex > len(self.colors)-1:
            self.colorIndex = 0
        self.config(bg=self.colors[self.colorIndex])


def main():
    root = Tk()
    root.title("Clicking Clicker")
    root.geometry("200x250")
    root.resizable(0, 0)

    app = App(root)
    root.mainloop()


main()
