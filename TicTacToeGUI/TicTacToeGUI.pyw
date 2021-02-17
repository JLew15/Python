import os
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd

HEIGHT = 500
WIDTH = 500


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH)
        self.createWidgets()

    def createWidgets(self):
        self.turn = "X"
        self.win = False
        self.layoutGrid = Frame(self)
        self.layoutGrid.grid()
        self.buttonGrid = Frame(self)
        self.buttonGrid.grid()
        self.outputGrid = Frame(self)
        self.outputGrid.grid()
        self.instructionsLabel = Label(self.layoutGrid,
                                       text="Welcome to Tic Tac Toe, click a button to take your turn.")
        menuBar = Menu(self.master)
        self.master.config(menu=menuBar)
        fileMenu = Menu(menuBar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menuBar.add_cascade(label="File", menu=fileMenu)
        self.instructionsLabel.grid(row=0, column=0, columnspan=3)
        self.tLButton = Button(self.buttonGrid, text=" ", width=5, height=2, command=self.topLeft)
        self.tLButton.grid(row=1, column=0)
        self.tMButton = Button(self.buttonGrid, text=" ", width=5, height=2, command=self.topMid)
        self.tMButton.grid(row=1, column=1)
        self.tRButton = Button(self.buttonGrid, text=" ", width=5, height=2, command=self.topRight)
        self.tRButton.grid(row=1, column=2)
        self.mLButton = Button(self.buttonGrid, text=" ", width=5, height=2, command=self.midLeft)
        self.mLButton.grid(row=2, column=0)
        self.mMButton = Button(self.buttonGrid, text=" ", width=5, height=2, command=self.midMid)
        self.mMButton.grid(row=2, column=1)
        self.mRButton = Button(self.buttonGrid, text=" ", width=5, height=2, command=self.midRight)
        self.mRButton.grid(row=2, column=2)
        self.bLButton = Button(self.buttonGrid, text=" ", width=5, height=2, command=self.botLeft)
        self.bLButton.grid(row=3, column=0)
        self.bMButton = Button(self.buttonGrid, text=" ", width=5, height=2, command=self.botMid)
        self.bMButton.grid(row=3, column=1)
        self.bRButton = Button(self.buttonGrid, text=" ", width=5, height=2, command=self.botRight)
        self.bRButton.grid(row=3, column=2)
        self.outputBox = Text(self.outputGrid, width=20, height=5)
        self.outputBox.grid(row=0, column=1)
        self.resetButton = Button(self.outputGrid, width=5, text="RESET", command=self.reset)
        self.resetButton.grid(row=1, column=1)

    def topLeft(self):
        self.checkWin()
        if self.turn == "X" and self.tLButton["text"] == " ":
            self.tLButton["text"] = "X"
            self.turn = "O"
        elif self.turn == "O" and self.tLButton["text"] == " ":
            self.tLButton["text"] = "O"
            self.turn = "X"
        else:
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "That space is taken. Please try a new one.")
        self.checkWin()


    def topMid(self):
        self.checkWin()
        if not self.win:
            if self.turn == "X" and self.tMButton["text"] == " ":
                self.tMButton["text"] = "X"
                self.turn = "O"
            elif self.turn == "O" and self.tMButton["text"] == " ":
                self.tMButton["text"] = "O"
                self.turn = "X"
            else:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "That space is taken. Please try a new one.")
        self.checkWin()

    def topRight(self):
        self.checkWin()
        if not self.win:
            if self.turn == "X" and self.tRButton["text"] == " ":
                self.tRButton["text"] = "X"
                self.turn = "O"
            elif self.turn == "O" and self.tRButton["text"] == " ":
                self.tRButton["text"] = "O"
                self.turn = "X"
            else:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "That space is taken. Please try a new one.")
        self.checkWin()

    def midLeft(self):
        self.checkWin()
        if not self.win:
            if self.turn == "X" and self.mLButton["text"] == " ":
                self.mLButton["text"] = "X"
                self.turn = "O"
            elif self.turn == "O" and self.mLButton["text"] == " ":
                self.mLButton["text"] = "O"
                self.turn = "X"
            else:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "That space is taken. Please try a new one.")
        self.checkWin()

    def midMid(self):
        self.checkWin()
        if not self.win:
            if self.turn == "X" and self.mMButton["text"] == " ":
                self.mMButton["text"] = "X"
                self.turn = "O"
            elif self.turn == "O" and self.mMButton["text"] == " ":
                self.mMButton["text"] = "O"
                self.turn = "X"
            else:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "That space is taken. Please try a new one.")
        self.checkWin()

    def midRight(self):
        self.checkWin()
        if not self.win:
            if self.turn == "X" and self.mRButton["text"] == " ":
                self.mRButton["text"] = "X"
                self.turn = "O"
            elif self.turn == "O" and self.mRButton["text"] == " ":
                self.mRButton["text"] = "O"
                self.turn = "X"
            else:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "That space is taken. Please try a new one.")
        self.checkWin()

    def botLeft(self):
        self.checkWin()
        if not self.win:
            if self.turn == "X" and self.bLButton["text"] == " ":
                self.bLButton["text"] = "X"
                self.turn = "O"
            elif self.turn == "O" and self.bLButton["text"] == " ":
                self.bLButton["text"] = "O"
                self.turn = "X"
            else:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "That space is taken. Please try a new one.")
        self.checkWin()

    def botMid(self):
        self.checkWin()
        if not self.win:
            if self.turn == "X" and self.bMButton["text"] == " ":
                self.bMButton["text"] = "X"
                self.turn = "O"
            elif self.turn == "O" and self.bMButton["text"] == " ":
                self.bMButton["text"] = "O"
                self.turn = "X"
            else:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "That space is taken. Please try a new one.")
        self.checkWin()

    def botRight(self):
        self.checkWin()
        if not self.win:
            if self.turn == "X" and self.bRButton["text"] == " ":
                self.bRButton["text"] = "X"
                self.turn = "O"
            elif self.turn == "O" and self.bRButton["text"] == " ":
                self.bRButton["text"] = "O"
                self.turn = "X"
            else:
                self.outputBox.delete(0.0, END)
                self.outputBox.insert(0.0, "That space is taken. Please try a new one.")
        self.checkWin()

    def checkWin(self):
        if self.tLButton["text"] == "X" and self.tMButton["text"] == "X" and self.tRButton["text"] == "X":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "X wins!")
            self.win = True
            self.mbPlayAgain()
        elif self.tLButton["text"] == "O" and self.tMButton["text"] == "O" and self.tRButton["text"] == "O":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "O wins!")
            self.win = True
            self.mbPlayAgain()

        elif self.mLButton["text"] == "X" and self.mMButton["text"] == "X" and self.mRButton["text"] == "X":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "X wins!")
            self.win = True
            self.mbPlayAgain()
        elif self.mLButton["text"] == "O" and self.mMButton["text"] == "O" and self.mRButton["text"] == "O":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "O wins!")
            self.win = True
            self.mbPlayAgain()

        elif self.bLButton["text"] == "X" and self.bMButton["text"] == "X" and self.bRButton["text"] == "X":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "X wins!")
            self.win = True
            self.mbPlayAgain()
        elif self.bLButton["text"] == "O" and self.bMButton["text"] == "O" and self.bRButton["text"] == "O":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "O wins!")
            self.win = True
            self.mbPlayAgain()

        elif self.tLButton["text"] == "X" and self.mLButton["text"] == "X" and self.bLButton["text"] == "X":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "X wins!")
            self.win = True
            self.mbPlayAgain()
        elif self.tLButton["text"] == "O" and self.mLButton["text"] == "O" and self.bLButton["text"] == "O":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "O wins!")
            self.win = True
            self.mbPlayAgain()

        elif self.tMButton["text"] == "X" and self.mMButton["text"] == "X" and self.bMButton["text"] == "X":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "X wins!")
            self.win = True
            self.mbPlayAgain()
        elif self.tMButton["text"] == "O" and self.mMButton["text"] == "O" and self.bMButton["text"] == "O":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "O wins!")
            self.win = True
            self.mbPlayAgain()

        elif self.tRButton["text"] == "X" and self.mRButton["text"] == "X" and self.bRButton["text"] == "X":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "X wins!")
            self.win = True
            self.mbPlayAgain()
        elif self.tRButton["text"] == "O" and self.mRButton["text"] == "O" and self.bRButton["text"] == "O":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "O wins!")
            self.win = True
            self.mbPlayAgain()

        elif self.tLButton["text"] == "X" and self.mMButton["text"] == "X" and self.bRButton["text"] == "X":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "X wins!")
            self.win = True
            self.mbPlayAgain()
        elif self.tLButton["text"] == "O" and self.mMButton["text"] == "O" and self.bRButton["text"] == "O":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "O wins!")
            self.win = True
            self.mbPlayAgain()

        elif self.tRButton["text"] == "X" and self.mMButton["text"] == "X" and self.bLButton["text"] == "X":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "X wins!")
            self.win = True
            self.mbPlayAgain()
        elif self.tRButton["text"] == "O" and self.mMButton["text"] == "O" and self.bLButton["text"] == "O":
            self.outputBox.delete(0.0, END)
            self.outputBox.insert(0.0, "O wins!")
            self.win = True
            self.mbPlayAgain()
        else:
            pass

    def mbPlayAgain(self):
        result = mb.askquestion("Play Again", "Do you want to play again?")

        if result == "yes":
            self.reset()
        else:
            quit()

    def reset(self):
        self.win = False
        self.tLButton["text"] = " "
        self.tMButton["text"] = " "
        self.tRButton["text"] = " "
        self.mLButton["text"] = " "
        self.mMButton["text"] = " "
        self.mRButton["text"] = " "
        self.bLButton["text"] = " "
        self.bMButton["text"] = " "
        self.bRButton["text"] = " "
        self.outputBox.delete(0.0, END)
        self.turn = "X"

    def onOpen(self):
        ftypes = [("Python file", "*.pyw")]
        dialog = fd.Open(self, filetypes=ftypes)
        f1 = dialog.show()
        if ".py" in f1:
            self.master.destroy()
            os.system("python "+f1)



def main():
    root = Tk()
    app = App(root)
    root.mainloop()


main()
