import random

def travel(pace,weather,health):
    speed = 0
    weatherMod = 0
    hours = 0
    if pace == "fast":
        speed = 4
    elif pace == "slow":
        speed = 1
    else:
        speed = 2
    if health == "poor":
        hours = 2
    elif health == "fair":
        hours = 4
    else:
        hours = 8
    if weather == "blizzard":
        weatherMod = 0
    elif weather == "hot":
        weatherMod = .5
    elif weather == "rain":
        weatherMod = .25
    else:
        weatherMod = 1
    miles = hours * speed * weatherMod
    randomMod = random.randint(0,5)
    return miles-randomMod

weather = "good"
health = "good"
pace = "normal"
miles = travel(pace,weather,health)
print(miles)
