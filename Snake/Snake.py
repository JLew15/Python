import random
import sys
from tkinter import *
from PIL import ImageTk, Image


class Constants:
    BOARD_WIDTH = 380
    BOARD_HEIGHT = 300
    DELAY = 100
    DOTSIZE = 10
    MAXRANNUM = 27


class Board(Canvas):
    def __init__(self):
        super(Board, self).__init__(width=Constants.BOARD_WIDTH, height=Constants.BOARD_HEIGHT, background="BLACK",
                                    highlightthickness=0)
        self.initGame()
        self.pack()

    def initGame(self):
        """INITIALIZE GAME"""
        self.inGame = True
        self.dots = 3
        self.score = 0

        self.moveX = Constants.DOTSIZE
        self.moveY = 0

        self.appleX = 100
        self.appleY = 190

        self.loadImages()

        self.createObjects()

        self.locateApple()
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Constants.DELAY, self.onTimer)

    def onKeyPressed(self, e):
        key = e.keys
        LEFTCURSORKEY = "Left"
        if key == LEFTCURSORKEY and self.moveX <= 0:
            self.moveX = -Constants.DOTSIZE
            self.moveY = 0
        RIGHTCURSORKEY = "Right"
        if key == RIGHTCURSORKEY and self.moveX >= 0:
            self.moveX = Constants.DOTSIZE
            self.moveY = 0
        UPCURSORKEY = "Up"
        if key == UPCURSORKEY and self.moveY <= 0:
            self.moveX = 0
            self.moveY = -Constants.DOTSIZE
        DOWNCURSORKEY = "Down"
        if key == DOWNCURSORKEY and self.moveY >= 0:
            self.moveX = 0
            self.moveY = Constants.DOTSIZE

    def onTimer(self):
        self.drawScore()
        self.checkCollision()

        if self.inGame:
            self.checkAppleCollision()
            self.moveSnake()
            self.after(Constants.DELAY, self.onTimer)
        else:
            self.gameOver()

    def moveSnake(self):
        pass

    def gameOver(self):
        pass

    def checkCollision(self):
        pass

    def checkAppleCollision(self):
        pass

    def drawScore(self):
        pass

    def loadImages(self):
        """Load images."""
        try:
            self.iBody = Image.open("Body1.png")
            self.iHead = Image.open("Head1.png")
            self.iApple = Image.open("Apple1.png")

            self.body = ImageTk.PhotoImage(self.iBody)
            self.head = ImageTk.PhotoImage(self.iHead)
            self.apple = ImageTk.PhotoImage(self.iApple)
        except IOError as e:
            print(e)
            sys.exit(1)

    def createObjects(self):
        self.create_text(30, 10, text="Score: {0}".format(self.score), tag="score", fill="white")
        self.create_image(self.appleX, self.appleY, image=self.apple, anchor=NW, tag="apple")
        self.create_image(50, 50, image=self.head, anchor=NW, tag="head")
        self.create_image(30, 50, image=self.body, anchor=NW, tag="body")
        self.create_image(40, 50, image=self.body, anchor=NW, tag="body")

    def locateApple(self):
        apple = self.find_withtag("apple")
        self.delete(apple[0])
        r = random.randint(0, Constants.MAXRANNUM)
        self.appleX = r * Constants.DOTSIZE
        r = random.randint(0, Constants.MAXRANNUM)
        self.appleY = r * Constants.DOTSIZE

        self.create_image(self.appleX, self.appleY, anchor=NW, image=self.apple, tag="apple")


class Snake(Frame):
    def __init__(self, master):
        super(Snake, self).__init__(master)
        self.master.title("Snake Game")
        self.board = Board()
        self.pack()


def main():
    root = Tk()
    snake = Snake(root)
    root.mainloop()


main()
