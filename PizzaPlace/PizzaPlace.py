from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.createWidgets(master)

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
        Checkbutton(self, text="Pepperoni", variable=self.pepperoni).grid(row=6, column=1, sticky=W)
        self.cheese = BooleanVar()
        Checkbutton(self, text="Cheese", variable=self.cheese).grid(row=6, column=2, sticky=W)
        self.sauce = BooleanVar()
        Checkbutton(self, text="Sauce", variable=self.sauce).grid(row=6, column=3, sticky=W)
        self.sausage = BooleanVar()
        Checkbutton(self, text="Sausage", variable=self.sausage).grid(row=6, column=4, sticky=W)

        Label().grid(row=7)

        self.order = Button(self, text="Order", bg="#ABCDEF", width=30, command=self.order)
        self.order.grid(row=8, column=2)

        self.output = Text(self)
        self.output.grid(row=9, columnspan=6)

    def order(self):
        message = "Your order is a " + self.pizzaSize.get() + " " + self.pizzaCrust.get() + " Crust pizza with the" \
                                                                                            " following toppings:"
        if self.pepperoni.get():
            message += "\nPepperoni"
        if self.cheese.get():
            message += "\nCheese"
        if self.sauce.get():
            message += "\nSauce"
        if self.sausage.get():
            message += "\nSausage"
        elif not self.pepperoni.get() and not self.cheese.get() and not self.sauce.get() and not self.sausage.get():
            message = "You can't order just dough... sorry."
        self.output.delete(0.0, END)
        self.output.insert(0.0, message)


def main():
    root = Tk()
    root.title("Sample Survey")
    root.geometry("720x485")
    root.attributes("-fullscreen", False)
    app = App(root)
    root.mainloop()


main()
