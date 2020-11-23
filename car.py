class Car():

    def __init__(self):
        self.color = ""
        self.size = ""
        self.brand = ""
        self.make = ""
        self.tireBrand = ""
        self.tireSize = ""
        self.type = ""
        self.price = 0.0
        self.drivetrain = ""
        self.makeYear = 0
        self.fuelType = ""
        self.engine = Engine()
        #self.radio = Radio()
        self.color = input("What color is your car? ")
        self.size = input("What size? ")
        self.brand = input("What brand? ")
        self.make = input("What make? ")
        self.tireBrand = input("What tire brand? ")
        self.tireSize = input("What tire size? ")
        self.type = input("Is your car a SUV, Truck, Sports Car or something else? ")
        self.price = float(input("Name your price. "))
        self.drivetrain = input("Is your car an automatic or manual? ")
        self.makeYear = int(input("What year was it made? "))
        self.fuelType = input("What fuel does it take? ")
    def display(self):
            print(self.color)
            print(self.size)
            print(self.brand)
            print(self.make)
            print(self.tireBrand)
            print(self.tireSize)
            print(self.type)
            print(self.price)
            print(self.drivetrain)
            print(self.makeYear)
            print(self.fuelType)
            print(self.engine.cylinders)
            print(self.engine.size)
            print(self.engine.cylinderOrientation)
            print(self.engine.mpg)


class Engine():
    def __init__(self):
        self.cylinders = 0
        self.size = ""
        self.cylinderOrientation = ""
        self.mpg = 0
        self.cylinders = int(input("How many cylinders does your engine have? "))
        self.size = input("How big is your engine? ")
        self.cylinderOrientation = input("What orientation are the cylinders? ")
        self.mpg = int(input("How many miles per gallon? Whole number only... "))

#class Radio():
#    def __init__(self):


def main():
    car1 = Car()
    car1.display()


main()
