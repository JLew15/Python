class Critter(object):
    """this is the class that defines what a critter is"""

    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = 0
        self.name = ""
        self.happy = 50
        self.isAlive = True

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

    def getName(self):
        return self.name

    def setHeight(self, height):
        if 5 > height > 1:
            self.height = height

    def getHealth(self):
        return self.health

    def getHunger(self):
        return self.hunger

    def getHappy(self):
        return self.happy

    def die(self):
        print(self.getName() + " has died...")
        self.health = 0
        self.isAlive = False

    def hud(self):
        print(self.getName())

        health = self.getHealth()
        if health > 80:
            print("Health: Great")
        elif health > 60:
            print("Health: Good")
        elif health > 50:
            print("Health: Fair")
        elif health == 0:
            self.die()
        else:
            print("Health: Poor")

        hunger = self.getHunger()
        if hunger > 40:
            print("Hunger: Starving")
        elif hunger > 20:
            print("Hunger: Really Hungry")
        elif hunger < 10:
            print("Hunger: Full")
        else:
            print("Hunger: Hungry")
        if hunger == 100:
            self.die()

        happy = self.getHappy()
        if happy >= 100:
            print("Happy: Extremely Happy")
        elif happy > 80:
            print("Happy: Super Happy")
        elif happy > 60:
            print("Happy: Pretty Happy")
        elif happy > 40:
            print("Happy: Happy")
        elif happy > 20:
            print("Happy: Modest")
        elif happy > 10:
            print("Happy: Sad")
        else:
            print("Happy: Depressed")


def main():
    critter1 = Critter()
    name = input("What will you name your pet?")
    critter1.setName(name)
    height = int(input("What is your pet's height?"))
    critter1.setHeight(height)
    critter1.intro()
    critter1.hud()
    while critter1.isAlive:
        critter1.passTime(1)
        print("What do you want to do?")
        print("Feed")
        print("Play")
        print("Nothing")
        response = input()
        if response == "feed" or response == "Feed":
            food = input("What do you want to feed your pet?")
            critter1.feed(food)
        elif response == "play" or response == "Play":
            time = int(input("How long will you play with your pet?"))
            critter1.play(time)
        critter1.hud()


main()
