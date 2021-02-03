from tkinter import *
from datetime import datetime


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets(master)
        self.timeNow = datetime.now()
        self.fmTimeNow = self.timeNow.strftime("%m/%d/%Y %H:%M:%S")


    def createWidgets(self, master):
        Label(self, text="Customer Name: ").grid(row=0, column=0, sticky=W)
        self.nameEntry = Entry(self)
        self.nameEntry.grid(row=0, column=1, columnspan=4, sticky=W)

        Label(self).grid(row=1)

        Label(self, text="Pizza Size: ").grid(row=1, column=0, sticky=W)
        self.pizzaSize = StringVar()
        self.pizzaSize.set("Large")
        Radiobutton(self, text="Small", value="Small", variable=self.pizzaSize).grid(row=1, column=1, sticky=W)
        Radiobutton(self, text="Medium", value="Medium", variable=self.pizzaSize).grid(row=1, column=2, sticky=W)
        Radiobutton(self, text="Large", value="Large", variable=self.pizzaSize).grid(row=1, column=3, sticky=W)

        Label(self).grid(row=3)

        Label(self, text="Crust Type: ").grid(row=4, column=0, sticky=W)
        self.pizzaCrust = StringVar()
        self.pizzaCrust.set("Thin")
        Radiobutton(self, text="Thin", value="Thin", variable=self.pizzaCrust).grid(row=4, column=1, sticky=W)
        Radiobutton(self, text="Thick", value="Thick", variable=self.pizzaCrust).grid(row=4, column=2, sticky=W)
        Radiobutton(self, text="Deep Dish", value="Deep Dish", variable=self.pizzaCrust).grid(
            row=4,
            column=3,
            sticky=W)
        Label(self).grid(row=5)

        Label(self, text="Toppings: ").grid(row=6, column=0, sticky=W)
        self.pepperoni = BooleanVar()
        self.cheese = BooleanVar()
        self.sauce = BooleanVar()
        self.sausage = BooleanVar()
        self.peppers = BooleanVar()
        self.olives = BooleanVar()
        self.anchovies = BooleanVar()
        self.bacon = BooleanVar()
        self.mushrooms = BooleanVar()
        self.steak = BooleanVar()
        self.ham = BooleanVar()
        self.pineapple = BooleanVar()
        self.extraCheese = BooleanVar()
        self.extraPepperoni = BooleanVar()
        self.lightSauce = BooleanVar()
        self.lightCheese = BooleanVar()

        Label().grid(row=10)

        self.order = Button(self, text="Order", bg="#ABCDEF", width=30, command=self.order)
        self.order.grid(row=11, column=0, columnspan=5)

        self.output = Text(self)
        self.output.grid(row=12, columnspan=5)
        self.price = 0.00

        self.textList = ["Pepperoni",
                        "Cheese",
                        "Sauce",
                        "Sausage",
                        "Peppers",
                        "Olives",
                        "Anchovies",
                        "Bacon",
                        "Mushrooms",
                        "Steak",
                        "Ham",
                        "Pineapple",
                        "Extra Cheese",
                        "Extra Pepperoni",
                        "Light Sauce",
                        "Light Cheese"]

        self.varList = [self.pepperoni,
                        self.cheese,
                        self.sauce,
                        self.sausage,
                        self.peppers,
                        self.olives,
                        self.anchovies,
                        self.bacon,
                        self.mushrooms,
                        self.steak,
                        self.ham,
                        self.pineapple,
                        self.extraCheese,
                        self.extraPepperoni,
                        self.lightSauce,
                        self.lightCheese]
        self.i = 0

        for r in range(4):
            for c in range(4):
                self.createCheck(self.textList[self.i], self.varList[self.i], r+6, c+1)
                self.i += 1

    def createCheck(self, words, var, r, c):
        Checkbutton(self,
                    text=words,
                    variable=var,
                    ).grid(row=r, column=c, sticky=W)

    def order(self):
        self.orders = open("orders.txt", "a")
        message = "Hello, " + self.nameEntry.get() + "! " + "Your order is a " + self.pizzaSize.get() + " " +\
                                                                                self.pizzaCrust.get()\
                                                                                + " Crust pizza with the" \
                                                                                " following toppings:"

        if self.pizzaSize.get() == "Small":
            self.price += 5.50
        elif self.pizzaSize.get() == "Medium":
            self.price += 7.50
        elif self.pizzaSize.get() == "Large":
            self.price += 10.00

        if self.pizzaCrust.get() == "Thin":
            self.price += 0.25
        elif self.pizzaCrust.get() == "Thick":
            self.price += 0.75
        elif self.pizzaCrust.get() == "Deep Dish":
            self.price += 1.75

        if self.pepperoni.get():
            message += "\nPepperoni"
            self.price += 0.5
        if self.cheese.get():
            message += "\nCheese"
            self.price += 0.5
        if self.sauce.get():
            message += "\nSauce"
            self.price += 0.5
        if self.sausage.get():
            message += "\nSausage"
            self.price += 0.5
        if self.peppers.get():
            message += "\nPeppers"
            self.price += 0.5
        if self.olives.get():
            message += "\nOlives"
            self.price += 0.5
        if self.anchovies.get():
            message += "\nAnchovies"
            self.price += 1.0
        if self.bacon.get():
            message += "\nBacon"
            self.price += 1.5
        if self.mushrooms.get():
            message += "\nMushrooms"
            self.price += 0.5
        if self.steak.get():
            message += "\nSteak"
            self.price += 2.0
        if self.ham.get():
            message += "\nHam"
            self.price += 1.0
        if self.pineapple.get():
            message += "\nPineapple"
            self.price += 0.5
        if self.extraCheese.get():
            message += "\nExtra Cheese"
            self.price += 0.5
        if self.extraPepperoni.get():
            message += "\nExtra Pepperoni"
            self.price += 0.5
        if self.lightSauce.get():
            message += "\nLight Sauce"
            self.price += 0.25
        if self.lightCheese.get():
            message += "\nLight Cheese"
            self.price += 0.25

        elif not self.pepperoni.get() and not self.cheese.get() and not self.sauce.get() and not self.sausage.get() and\
                not self.peppers.get() and not self.olives.get() and not self.anchovies.get() and not self.bacon.get()\
                and not self.mushrooms.get() and not self.steak.get() and not self.ham.get() and not \
                self.pineapple.get() and not self.extraCheese.get() and not self.extraPepperoni.get() and not \
                self.lightSauce.get() and not self.lightCheese.get():
            message = "You can't order just dough... sorry."
        if self.nameEntry.get() == "":
            message = "Please enter a name first."
        self.output.delete(0.0, END)
        self.output.insert(0.0, message + "\n\nyour total is: " + str(self.price))
        self.orders.write("\n\n"+ "ORDER AT " + str(self.fmTimeNow) + "\n" + message + "\n\nyour total is: " + str(self.price) + "\n__________________________")
        self.orders.close()
        self.price = 0.0



def main():
    root = Tk()
    root.title("Sample Survey")
    root.geometry("720x685")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()


main()
