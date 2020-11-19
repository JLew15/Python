def rest(health,rations,current_day):
    try:
        days = int(input("How many days do you want to rest"))
        if rations == "full":
            health_mod = 2
        elif rations == "half":
            health_mod = 1
        elif rations == "quarter":
            health_mod = .5
        current_day += days
    except:
        print("not a good option")
    health_gain = 10 * days * health_mod
    if (health_gain + health) > 100:
        health = 100
    else:
        health += health_gain

    return health,current_day

health = 50
rations = "half"
current_day = 1
health, current_day = rest(health,rations,current_day)
print(health)
print(current_day)
