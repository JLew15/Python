from tkinter import *
from tkinter import messagebox as mb

HEIGHT = 500
WIDTH = 500


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.error = Button(self, text="Error", command=self.onError)
        self.error.grid()
        self.warning = Button(self, text="Warning", command=self.onWarning)
        self.warning.grid()
        self.question = Button(self, text="Question", command=self.onQuestion)
        self.question.grid()
        self.inform = Button(self, text="Information", command=self.onInfo)
        self.inform.grid()

    def onError(self):
        mb.showerror("Error", "Could not open File.")

    def onWarning(self):
        mb.showwarning("Warning", "Deprecated function call")

    def onQuestion(self):
        result = mb.askquestion("Question", "Are you sure you want to quit?")

        if result == "yes":
            print("You clicked yes.")
        else:
            print("You clicked no.")

    def onInfo(self):
        mb.showinfo("Information", "Download Complete.")


def main():
    root = Tk()
    root.geometry(str(HEIGHT)+"x"+str(WIDTH))
    app = App(root)
    root.mainloop()

main()