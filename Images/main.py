from tkinter import *
from PIL import Image, ImageTk

HEIGHT = 300
WIDTH = 250



class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH, expand=1)
        self.createWidgets()
        self.i = 0

    def createWidgets(self):
        self.config(bg="cornflowerblue")
        self.pLabel = Label(text="These are some cool call of duty images.")
        self.pLabel.place(x=20)
        self.picButton = Button(text="Switch Image", command=self.switchImage)
        self.picButton.place(x=80, y=30)

        img1 = Image.open("CodPoints.jpg")
        img2 = Image.open("Alex.png")
        img3 = Image.open("Season1BP.png")

        cod = ImageTk.PhotoImage(img1)
        alex = ImageTk.PhotoImage(img2)
        season1 = ImageTk.PhotoImage(img3)

        self.imageList = [cod, alex, season1]

        # imgLabel1 = Label(self, image=cod)
        # imgLabel1.image = cod
        # imgLabel1.place(x=25, y=75)
        # imgLabel2 = Label(self, image=alex)
        # imgLabel2.image = alex
        # imgLabel2.place(x=25, y=292)
        # imgLabel3 = Label(self, image=season1)
        # imgLabel3.image = season1
        # imgLabel3.place(x=25, y=510)

    def switchImage(self):
        if self.i < len(self.imageList):
            imgLabel = Label(self, image=self.imageList[self.i])
            imgLabel.place(x=25, y=75)
        else:
            self.i = 0
            imgLabel = Label(self, image=self.imageList[self.i])
            imgLabel.place(x=25, y=75)
        self.i += 1


def main():
    root = Tk()
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    app = App(root)
    root.mainloop()


main()
