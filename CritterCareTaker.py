class Critter(object):
    """this is the class that defines what a critter is"""

    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = 0
        self.name = ""
        self.happy = 50

    def intro(self):
        print("Hello, my name is", self.name)

    def feed(self, food):
        if food == "pizza":
            self.hunger -= 7
        elif food == "cheeseburger":
            self.hunger -= 13
        elif food == "steak":
            self.hunger -= 23
        elif food == "corn":
            self.hunger -= 3
        elif food == "pizza burger":
            self.hunger -= 20
        elif food == "cheesecake":
            self.hunger -= 100
        else:
            self.hunger -= 5

    def passTime(self, hours):
        for i in range(hours):
            self.hunger += 2
            if self.hunger < 0:
                self.weight += 1
                self.happy += 10
                self.health -= 5
            if self.hunger > 50:
                self.weight -= 1
                self.happy -= 10
                self.health -= 5
            self.happy -= 5

    def play(self, time):
        self.passTime(time)
        self.happy += 10*time
        if self.happy > 100:
            self.happy = 100
        self.health += 10 * time
        if self.health > 100:
            self.health = 100

    def getHunger(self):
        return self.hunger

    def setName(self, name):
        self.name = name

    def setHeight(self, height):
        self.height = height


def main():
    critter1 = Critter()
    critter1.name = "Silent Night"

    critter2 = Critter()
    critter2.name = "Silver Bells"

    critter1.intro()
    critter2.intro()


main()
