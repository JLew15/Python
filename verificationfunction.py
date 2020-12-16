import datetime


def getVerifiedInteger(message, low, high):
    var = 0
    while not low <= var <= high:
        var = int(input(message))
        if var >= high + 1 or var <= low - 1:
            print("Try again...")
    return var


month = getVerifiedInteger("Please enter today's month ", 1, 12)
day = getVerifiedInteger("Please enter today's day", 1, 31)
year = getVerifiedInteger("Please enter today's year", 2000, 2030)

today = datetime.date(year, month, day)
print("Today is a " + today.strftime("%A"))
