from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.titleLabel = Label(self, text="Sample Survey")
        self.titleLabel.grid(row=0, sticky=N)

        self.checkboxLabel = Label(self, text="Select all that apply:")
        self.checkboxLabel.grid(row=1, sticky=W)

        self.horror = BooleanVar()
        self.check1 = Checkbutton(self, text="Horror", variable=self.horror, command=self.update)
        self.check1.grid(row=2, column=0, sticky=W)

        self.humor = BooleanVar()
        self.check2 = Checkbutton(self, text="Humor/Funny", variable=self.humor, command=self.update)
        self.check2.grid(row=3, column=0, sticky=W)

        self.drama = BooleanVar()
        self.check3 = Checkbutton(self, text="Drama", variable=self.drama, command=self.update)
        self.check3.grid(row=4, column=0, sticky=W)

        self.worstGenre = StringVar()
        self.worstGenre.set(None)
        self.radio = Radiobutton(self, text="Romance", value="Romance Movies", variable=self.worstGenre, command=self.update)
        self.radio.grid(row=5, column=0, sticky=W)
        self.radio = Radiobutton(self, text="SciFi", value="SciFi Movies", variable=self.worstGenre, command=self.update)
        self.radio.grid(row=6, column=0, sticky=W)
        self.radio = Radiobutton(self, text="AA", value="AA Movies", variable=self.worstGenre, command=self.update)
        self.radio.grid(row=7, column=0, sticky=W)
        self.radio = Radiobutton(self, text="B", value="B Movies", variable=self.worstGenre, command=self.update)
        self.radio.grid(row=8, column=0, sticky=W)

        self.output = Text(self)
        self.output.grid(row=9, column=0)

    def update(self):
        likes = ""
        if self.horror.get():
            likes += " You like horror movies\n"
        if self.humor.get():
            likes += " You like funny movies\n"
        if self.drama.get():
            likes += " You like dramatic movies\n"
        likes += "Your least favorite movie genre is " + self.worstGenre.get()

        self.output.delete(0.0, END)
        self.output.insert(0.0, likes)


def main():
    root = Tk()
    root.title("Sample Survey")
    root.geometry("720x485")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()


main()
