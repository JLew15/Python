def rest(health,rations,current_day):
    try:
        days = int(input("How many days do you want to rest"))
        if rations == "full":
            healthMod = 2
        elif rations == "half":
            healthMod = 1
        elif rations == "quarter":
            healthMod = .5
        currentDay += days
    except:
        print("not a good option")
    healthGain = 10 * days * healthMod
    if (healthGain + health) > 100:
        health = 100
    else:
        health += healthGain

    return health,currentDay

health = 50
rations = "half"
currentDay = 1
health, currentDay = rest(health,rations,currentDay)
print(health)
print(currentDay)
