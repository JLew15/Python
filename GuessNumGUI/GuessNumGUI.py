from tkinter import *
import random


class App(Frame):
    diff = 1

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.maxNum = 10
        self.numTrys = 3
        self.theNumber = random.randint(1, self.maxNum)
        self.instructionlbl = Label(self, text="""I'm thinking of a number between 1 and 10,
         try to guess it in 3 attempts""")
        self.instructionlbl.grid(row=0, column=0, columnspan=2)
        self.onebutton = Button(self, text="1", command=self.onebuttonPress)
        self.onebutton.grid(row=1, column=0)
        self.twobutton = Button(self, text="2", command=self.twobuttonPress)
        self.twobutton.grid(row=1, column=1)
        self.threebutton = Button(self, text="3", command=self.threebuttonPress)
        self.threebutton.grid(row=2, column=0)
        self.fourbutton = Button(self, text="4", command=self.fourbuttonPress)
        self.fourbutton.grid(row=2, column=1)
        self.fivebutton = Button(self, text="5", command=self.fivebuttonPress)
        self.fivebutton.grid(row=3, column=0)
        self.sixbutton = Button(self, text="6", command=self.sixbuttonPress)
        self.sixbutton.grid(row=3, column=1)
        self.sevenbutton = Button(self, text="7", command=self.sevenbuttonPress)
        self.sevenbutton.grid(row=4, column=0)
        self.eightbutton = Button(self, text="8", command=self.eightbuttonPress)
        self.eightbutton.grid(row=4, column=1)
        self.ninebutton = Button(self, text="9", command=self.ninebuttonPress)
        self.ninebutton.grid(row=5, column=0)
        self.tenbutton = Button(self, text="10", command=self.tenbuttonPress)
        self.tenbutton.grid(row=5, column=1)
        self.outputBox = Text(self, width=30, height=5)
        self.outputBox.grid(row=6, column=0, columnspan=2)

    def onebuttonPress(self):
        if 1 != self.theNumber:
            self.numTrys -= 1
            if 1 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 1 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
        if self.numTrys <= 0:
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "YOU FAILED")
        elif self.numTrys > 0:
            if 1 == self.theNumber:
                self.numTrys = 3
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "You Got It")

    def twobuttonPress(self):
        if 2 != self.theNumber:
            self.numTrys -= 1
            if 2 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 2 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
            if self.numTrys <= 0:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "YOU FAILED")
            elif self.numTrys > 0:
                if 1 == self.theNumber:
                    self.numTrys = 3
                    self.outputBox.delete(0.0, END)
                    self.outputBox.insert(0.0, "You Got It")

    def threebuttonPress(self):
        if 3 != self.theNumber:
            self.numTrys -= 1
            if 3 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 3 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
            if self.numTrys <= 0:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "YOU FAILED")
            elif self.numTrys > 0:
                if 1 == self.theNumber:
                    self.numTrys = 3
                    self.outputBox.delete(0.0, END)
                    self.outputBox.insert(0.0, "You Got It")

    def fourbuttonPress(self):
        if 4 != self.theNumber:
            self.numTrys -= 1
            if 4 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 4 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
            if self.numTrys <= 0:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "YOU FAILED")
            elif self.numTrys > 0:
                if 1 == self.theNumber:
                    self.numTrys = 3
                    self.outputBox.delete(0.0, END)
                    self.outputBox.insert(0.0, "You Got It")

    def fivebuttonPress(self):
        if 5 != self.theNumber:
            self.numTrys -= 1
            if 5 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 5 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
            if self.numTrys <= 0:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "YOU FAILED")
            elif self.numTrys > 0:
                if 1 == self.theNumber:
                    self.numTrys = 3
                    self.outputBox.delete(0.0, END)
                    self.outputBox.insert(0.0, "You Got It")

    def sixbuttonPress(self):
        if 6 != self.theNumber:
            self.numTrys -= 1
            if 6 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 6 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
            if self.numTrys <= 0:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "YOU FAILED")
            elif self.numTrys > 0:
                if 1 == self.theNumber:
                    self.numTrys = 3
                    self.outputBox.delete(0.0, END)
                    self.outputBox.insert(0.0, "You Got It")

    def sevenbuttonPress(self):
        if 7 != self.theNumber:
            self.numTrys -= 1
            if 7 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 7 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
            if self.numTrys <= 0:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "YOU FAILED")
            elif self.numTrys > 0:
                if 1 == self.theNumber:
                    self.numTrys = 3
                    self.outputBox.delete(0.0, END)
                    self.outputBox.insert(0.0, "You Got It")

    def eightbuttonPress(self):
        if 8 != self.theNumber:
            self.numTrys -= 1
            if 8 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 8 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
            if self.numTrys <= 0:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "YOU FAILED")
            elif self.numTrys > 0:
                if 1 == self.theNumber:
                    self.numTrys = 3
                    self.outputBox.delete(0.0, END)
                    self.outputBox.insert(0.0, "You Got It")

    def ninebuttonPress(self):
        if 9 != self.theNumber:
            self.numTrys -= 1
            if 9 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 9 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
            if self.numTrys <= 0:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "YOU FAILED")
            elif self.numTrys > 0:
                if 1 == self.theNumber:
                    self.numTrys = 3
                    self.outputBox.delete(0.0, END)
                    self.outputBox.insert(0.0, "You Got It")

    def tenbuttonPress(self):
        if 10 != self.theNumber:
            self.numTrys -= 1
            if 10 < self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Higher")
            elif 10 > self.theNumber:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "Guess Lower")
            if self.numTrys <= 0:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "YOU FAILED")
            elif self.numTrys > 0:
                if 1 == self.theNumber:
                    self.numTrys = 3
                    self.outputBox.delete(0.0, END)
                    self.outputBox.insert(0.0, "You Got It")


def main():
    root = Tk()
    root.geometry("250x750")
    app = App(root)
    root.mainloop()


main()
