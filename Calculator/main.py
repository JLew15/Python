from tkinter import *

HEIGHT = 500
WIDTH = 500

value2Activated = False
divideActivated = False
multiplyActivated = False
subtractActivated = False
plusActivated = False


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH)
        self.createWidgets()

    def createWidgets(self):
        self.value1 = ""
        self.value2 = ""
        self.layoutGrid = Frame(self)
        self.layoutGrid.grid()
        self.instructionLabel = Label(self.layoutGrid, text="Please enter a number and push one of the operators.")
        self.instructionLabel.grid(row=0, column=0, sticky=N, columnspan=4)
        self.outputBox = Text(self.layoutGrid, width=30, height=5)
        self.outputBox.grid(row=1, column=0, columnspan=4)
        self.oneButton = Button(self.layoutGrid, text="1", width=5, height=2, command=self.oneButtonPress)
        self.oneButton.grid(row=4, column=0)
        self.twoButton = Button(self.layoutGrid, text="2", width=5, height=2, command=self.twoButtonPress)
        self.twoButton.grid(row=4, column=1)
        self.threeButton = Button(self.layoutGrid, text="3", width=5, height=2, command=self.threeButtonPress)
        self.threeButton.grid(row=4, column=2)
        self.fourButton = Button(self.layoutGrid, text="4", width=5, height=2, command=self.fourButtonPress)
        self.fourButton.grid(row=3, column=0)
        self.fiveButton = Button(self.layoutGrid, text="5", width=5, height=2, command=self.fiveButtonPress)
        self.fiveButton.grid(row=3, column=1)
        self.sixButton = Button(self.layoutGrid, text="6", width=5, height=2, command=self.sixButtonPress)
        self.sixButton.grid(row=3, column=2)
        self.sevenButton = Button(self.layoutGrid, text="7", width=5, height=2, command=self.sevenButtonPress)
        self.sevenButton.grid(row=2, column=0)
        self.eightButton = Button(self.layoutGrid, text="8", width=5, height=2, command=self.eightButtonPress)
        self.eightButton.grid(row=2, column=1)
        self.nineButton = Button(self.layoutGrid, text="9", width=5, height=2, command=self.nineButtonPress)
        self.nineButton.grid(row=2, column=2)
        self.zeroButton = Button(self.layoutGrid, text="0", width=5, height=2, command=self.zeroButtonPress)
        self.zeroButton.grid(row=6, column=1)
        self.equalsButton = Button(self.layoutGrid, text="=", width=5, height=2, command=self.equalsButtonPress)
        self.equalsButton.grid(row=6, column=2)
        self.plusButton = Button(self.layoutGrid, text="+", width=5, height=2, command=self.plusButtonPress)
        self.plusButton.grid(row=4, column=3)
        self.subtractButton = Button(self.layoutGrid, text="-", width=5, height=2, command=self.subtractButtonPress)
        self.subtractButton.grid(row=3, column=3)
        self.divideButton = Button(self.layoutGrid, text="/", width=5, height=2, command=self.divideButtonPress)
        self.divideButton.grid(row=2, column=3)
        self.multiplyButton = Button(self.layoutGrid, text="*", width=5, height=2, command=self.multiplyButtonPress)
        self.multiplyButton.grid(row=6, column=3)
        self.clearButton = Button(self.layoutGrid, text="C", width=5, height=2)#, command=self.clearButtonPress)
        self.clearButton.grid(row=6, column=0)

    def oneButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "1"
        else:
            self.value2 = self.value2 + "1"

    def twoButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "2"
        else:
            self.value2 = self.value2 + "2"

    def threeButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "3"
        else:
            self.value2 = self.value2 + "3"

    def fourButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "4"
        else:
            self.value2 = self.value2 + "4"

    def fiveButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "5"
        else:
            self.value2 = self.value2 + "5"

    def sixButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "6"
        else:
            self.value2 = self.value2 + "6"

    def sevenButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "7"
        else:
            self.value2 = self.value2 + "7"

    def eightButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "8"
        else:
            self.value2 = self.value2 + "8"

    def nineButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "9"
        else:
            self.value2 = self.value2 + "9"

    def zeroButtonPress(self):
        if not value2Activated:
            self.value1 = self.value1 + "0"
        else:
            self.value2 = self.value2 + "0"

    def plusButtonPress(self):
        value2Activated = True
        plusActivated = True

    def subtractButtonPress(self):
        value2Activated = True
        subtractActivated = True

    def multiplyButtonPress(self):
        value2Activated = True
        multiplyActivated = True

    def divideButtonPress(self):
        value2Activated = True
        divideActivated = True

    def equalsButtonPress(self):
        if not value2Activated:
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, self.value1)

def main():
    root = Tk()
    # root.geometry(str(HEIGHT)+"x"+str(WIDTH))
    app = App(root)
    root.mainloop()

main()
