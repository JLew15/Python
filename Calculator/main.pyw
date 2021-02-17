import os
from tkinter import *
from tkinter import filedialog as fd

HEIGHT = 500
WIDTH = 500




class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH)
        self.createWidgets()

    def createWidgets(self):
        self.value1 = "0"
        self.value2 = "0"
        self.finalValue = "0"
        self.message = ""
        self.value2Activated = False
        self.divideActivated = False
        self.multiplyActivated = False
        self.subtractActivated = False
        self.plusActivated = False
        menuBar = Menu(self.master)
        self.master.config(menu=menuBar)
        fileMenu = Menu(menuBar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menuBar.add_cascade(label="File", menu=fileMenu)
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
        self.clearButton = Button(self.layoutGrid, text="C", width=5, height=2, command=self.clearButtonPress)
        self.clearButton.grid(row=6, column=0)

    def oneButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "1"
        else:
            self.value2 = self.value2 + "1"
        self.message = self.message + "1"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def twoButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "2"
        else:
            self.value2 = self.value2 + "2"
        self.message = self.message + "2"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def threeButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "3"
        else:
            self.value2 = self.value2 + "3"
        self.message = self.message + "3"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def fourButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "4"
        else:
            self.value2 = self.value2 + "4"
        self.message = self.message + "4"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def fiveButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "5"
        else:
            self.value2 = self.value2 + "5"
        self.message = self.message + "5"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def sixButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "6"
        else:
            self.value2 = self.value2 + "6"
        self.message = self.message + "6"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def sevenButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "7"
        else:
            self.value2 = self.value2 + "7"
        self.message = self.message + "7"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def eightButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "8"
        else:
            self.value2 = self.value2 + "8"
        self.message = self.message + "8"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def nineButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "9"
        else:
            self.value2 = self.value2 + "9"
        self.message = self.message + "9"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def zeroButtonPress(self):
        if not self.value2Activated:
            self.value1 = self.value1 + "0"
        else:
            self.value2 = self.value2 + "0"
        self.message = self.message + "0"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def plusButtonPress(self):
        self.value2Activated = True
        self.plusActivated = True
        self.message = self.message + "+"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def subtractButtonPress(self):
        self.value2Activated = True
        self.subtractActivated = True
        self.message = self.message + "-"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def multiplyButtonPress(self):
        self.value2Activated = True
        self.multiplyActivated = True
        self.message = self.message + "*"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def divideButtonPress(self):
        self.value2Activated = True
        self.divideActivated = True
        self.message = self.message + "/"
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, self.message)

    def equalsButtonPress(self):
        if not self.value2Activated:
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, self.value1)
        elif self.value2Activated and self.multiplyActivated:
            self.finalValue = (int(self.value1)*int(self.value2))
            self.finalValue = str(self.finalValue)
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, self.finalValue)
        elif self.value2Activated and self.divideActivated:
            self.finalValue = (int(self.value1)/int(self.value2))
            self.finalValue = str(self.finalValue)
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, self.finalValue)
        elif self.value2Activated and self.plusActivated:
            self.finalValue = (int(self.value1)+int(self.value2))
            self.finalValue = str(self.finalValue)
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, self.finalValue)
        elif self.value2Activated and self.subtractActivated:
            self.finalValue = str((int(self.value1)-int(self.value2)))
            self.finalValue = str(self.finalValue)
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, self.finalValue)
        self.value1 = "0"
        self.value2 = "0"
        self.finalValue = "0"
        self.message = ""
        self.value2Activated = False
        self.subtractActivated = False
        self.plusActivated = False
        self.divideActivated = False
        self.multiplyActivated = False
    def clearButtonPress(self):
        self.value1 = "0"
        self.value2 = "0"
        self.finalValue = "0"
        self.message = ""
        self.value2Activated = False
        self.subtractActivated = False
        self.plusActivated = False
        self.divideActivated = False
        self.multiplyActivated = False
        self.outputBox.delete(0.0, END)
        self.outputBox.insert(0.0, "NUMBERS CLEARED")

    def onOpen(self):
        ftypes = [("Python file", "*.pyw")]
        dialog = fd.Open(self, filetypes=ftypes)
        f1 = dialog.show()
        if ".py" in f1:
            self.master.destroy()
            os.system("python "+f1)


def main():
    root = Tk()
    # root.geometry(str(HEIGHT)+"x"+str(WIDTH))
    app = App(root)
    root.mainloop()

main()
