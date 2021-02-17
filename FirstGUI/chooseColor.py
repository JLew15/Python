from tkinter import *
from tkinter import colorchooser

HEIGHT = 500
WIDTH = 500


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH, expand=1)
        self.createWidgets()

    def createWidgets(self):
        self.bttn = Button(self, text="Choose Color", command=self.onChoose)
        self.bttn.place(x=30, y=30)

        self.frame = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.frame.place(x=160, y=30)

    def onChoose(self):
        (rgb, hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)


def main():
    root = Tk()
    app = App(root)
    root.mainloop()

main()