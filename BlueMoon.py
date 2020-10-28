moon = input("Is there a blue moon tonight? (Yes/No)? ")
weekday = input("What day of the week is it? (Monday - Sunday) ")
monthday = int(input("What day of the month is it? (1-31) "))
song = ""
if moon.upper() == "YES":
    song = "Once in a Blue Moon"
    print("Play song "+song)

elif moon.upper() == "NO":
    if weekday.upper() == "MONDAY":
        song = "Manic Monday"
        if int(monthday) >= 15:
            song = "Day Dream Believer"
            print("Play song "+song)
        else:
            print("Play song "+song)


    elif weekday.upper() == "TUESDAY":
        song = "Tuesday's Gone"
        print("Play song "+song)
        if monthday >= 15:
            song = "Day Dream Believer"
        else:
            print("Play song "+song)


    elif weekday.upper() == "WEDNESDAY":
        song = "Just Wednesday"
        if monthday >= 15:
            song = "Day Dream Believer"
            print("Play song "+song)
        else:
            print("Play song "+song)


    elif weekday.upper() == "THURSDAY":
        song = "Sweet Thursday"
        if monthday >= 15:
            song = "Day Dream Believer"
            print("Play song "+song)
        else:
            print("Play song "+song)


    elif weekday.upper() == "FRIDAY":
        song = "Friday I'm in Love"
        if monthday >= 15:
            song = "Day Dream Believer"
            print("Play song "+song)
        else:
            print("Play song "+song)


    elif weekday.upper() == "SATURDAY":
        song = "Saturday in the Park"
        if monthday >= 15:
            song = "Day Dream Believer"
            print("Play song "+song)
        else:
            print("Play song "+song)


    elif weekday.upper() == "SUNDAY":
        song = "Lazing on a Sunday Afternoon"
        if monthday >= 15:
            song = "Day Dream Believer"
            print("Play song "+song)
        else:
            print("Play song "+song)


    else:
        song = "Days of the Week"
        print("Play song "+song)
