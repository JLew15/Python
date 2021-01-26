from tkinter import *
import os
import time

entrance = False
messageRan = False


class Clicker(Frame):
    def __init__(self, master):
        super(Clicker, self).__init__(master)
        self.grid()
        self.total = 0
        self.colors = ["#000000", "#FFFFFF", "#F00000", "#0F0000", "#00F000", "#000F00", "#0000F0", "#00000F"]
        self.colorIndex = 0
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self, text="Total People:")
        self.label2 = Label(self, text=str(self.total))
        self.buttonAdd = Button(self, text="+ Person")
        self.buttonAdd.config(command=self.addToCount)
        self.buttonRm = Button(self, text="- Person")
        self.buttonRm.config(command=self.rmFromCount)
        self.buttonColor = Button(self, text="Change Color", width=28, height=5)
        self.buttonColor.config(command=self.changeColor)

        self.label1.grid()
        self.label2.grid()
        self.buttonAdd.grid()
        self.buttonRm.grid()
        self.buttonColor.grid()

    def addToCount(self):
        self.total += 1
        if 10 > self.total > 0:
            self.label1.config(bg="green")
        elif 9 < self.total < 25:
            self.label1.config(bg="yellow")
        elif self.total > 25:
            self.label1.config(bg="red")
        print(self.total)
        self.label2.config(text=str(self.total))

    def rmFromCount(self):
        self.total -= 1
        if self.total < 0:
            self.label1.config(bg="pink")
        elif 10 > self.total > 0:
            self.label1.config(bg="green")
        elif 9 < self.total < 25:
            self.label1.config(bg="yellow")
        elif self.total > 25:
            self.label1.config(bg="red")
        print(self.total)
        self.label2.config(text=str(self.total))

    def changeColor(self):
        self.colorIndex += 1
        if self.colorIndex > len(self.colors) - 1:
            self.colorIndex = 0
        self.config(bg=self.colors[self.colorIndex])


class App(Frame):
    usernames = ["jayjay223", "johnnysilverhand123"]
    passwords = ["HeheWow", "HeresJohnny"]
    entrance = False

    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets()
        self.tries = 0
        self.showingPass = False

    def createWidgets(self):
        self.lbl = Label(self, text="Enter your password.")
        self.lbl.grid(row=0, column=0, columnspan=3, sticky=N)
        self.userlbl = Label(self, text="Username")
        self.userlbl.grid(row=1, sticky=W)
        self.passlbl = Label(self, text="Password")
        self.passlbl.grid(row=2, sticky=W)
        self.bttn = Button(self, text="BUTTON")
        self.bttn.grid(row=3)
        self.bttn["command"] = self.submit
        self.userEntry = Entry(self)
        self.userEntry.grid(row=1, column=1, columnspan=2)
        self.passEntry = Entry(self, show="*")
        self.passEntry.grid(row=2, column=1, columnspan=2)
        self.txtArea = Text(self)
        self.txtArea.grid(row=4, columnspan=3)
        self.showPass = Button(self, text="Show Password", command=self.passShow)
        self.showPass.grid(row=2, column=2)

    def submit(self):
        self.username = self.userEntry.get()
        self.password = self.passEntry.get()
        if self.username.lower() in self.usernames:
            index = self.usernames.index(self.username)
            if self.password == self.passwords[index]:
                self.tries = 0
                self.entrance = True
                message = "You got in :)"
                self.showMessage(message)
                self.Load()



            else:
                message = "Incorrect Password."
                self.tries += 1
                self.showMessage(message)
        else:
            message = "Incorrect Username"
            self.tries += 1
            self.showMessage(message)
        if self.tries > 3:
            message = "Sorry man... you just gotta stop. You've been locked out."
            self.showMessage(message)
            self.bttn["command"] = self.lockout

    def Load(self):
        time.sleep(2)
        if messageRan:
            self.destroy()

    def showMessage(self,message):
        self.txtArea.delete(0.0, END)
        self.txtArea.insert(0.0, message, END)
        time.sleep(1)
        global messageRan
        messageRan = True
        time.sleep(1)

    def passShow(self):
        if not self.showingPass:
            self.passEntry["show"] = ""
            self.showingPass = True
        elif self.showingPass:
            self.passEntry["show"] = "*"
            self.showingPass = False

    def lockout(self):
        self.userEntry["bg"] = "#000000"
        self.passEntry["bg"] = "#000000"
        self.bttn["bg"] = "#000000"


def main():
    root = Tk()
    root.title("Password Entry")
    root.geometry("720x485")
    root.attributes("-fullscreen", False)
    root.resizable(0, 0)
    container = Frame(root)
    container.grid()
    app = App(container)
    app1 = Clicker(container)
    app.grid(row=0, column=0)

    root.mainloop()


main()
