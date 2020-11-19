import random

def travel(pace,weather,health):
    speed = 0
    weather_mod = 0
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
        weather_mod = 0
    elif weather == "hot":
        weather_mod = .5
    elif weather == "rain":
        weather_mod = .25
    else:
        weather_mod = 1
    miles = hours * speed * weather_mod
    random_mod = random.randint(0,5)
    return miles-random_mod

weather = "good"
health = "good"
pace = "normal"
miles = travel(pace,weather,health)
print(miles)
