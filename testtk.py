from tkinter import *
from tkinter.ttk import *

HEIGHT = 500
WIDTH = 500


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=X)
        self.createWidgets()

    def createWidgets(self):
        itemsList = [1, 2, 3, 4, 5, "hello"]
        self.cb = Combobox(self, values=itemsList)
        # self.cb.config(values=itemsList)
        # self.cb["values"] = itemsList
        self.cb.current(0)
        self.cb.pack()

        self.button1 = Button(self, text="Try Me", command=self.onChangeValues)
        self.button1.pack()

        self.lbox = Listbox(self)
        listItems = [1, 2, 3, 4, 5, 6, 7]
        for i in range(len(listItems)):
            self.lbox.insert(i, listItems[i])
        self.lbox["selectmode"] = EXTENDED
        self.lbox.pack()

        self.pgBar = Progressbar(self, length=200, value=50)
        self.pgBar.pack()

        self.pgIncrease = Button(text="^", command=self.increase)
        self.pgIncrease.pack()
        self.pgDecrease = Button(text="ˇ", command=self.decrease)
        self.pgDecrease.pack()

    def onChangeValues(self):
        cdText = self.cb.get()
        print(cdText)
        x=""
        lbCurrent = self.lbox.curselection()
        for i in lbCurrent:
            x += str(self.lbox.get(i))
        print(str(x))

    def increase(self):
        self.pgBar["value"] = self.pgBar["value"]+1

    def decrease(self):
        self.pgBar["value"] = self.pgBar["value"]-1



def main():
    root = Tk()
    # root.geometry(str(HEIGHT)+"x"+str(WIDTH))
    root.title("More widgets")
    app = App(root)
    root.mainloop()

main()
