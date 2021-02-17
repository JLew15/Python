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
        menuBar = Menu(self.master)
        self.master.config(menu=menuBar)
        fileMenu = Menu(menuBar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menuBar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):
        ftypes = [("Python file", "*.py")]
        dialog = fd.Open(self, filetypes=ftypes)
        f1 = dialog.show()
        if ".py" in f1:
            os.system("python "+f1)


def main():
    root = Tk()
    root.geometry(str(HEIGHT)+"x"+str(WIDTH))
    app = App(root)
    root.mainloop()

main()