import time
import sys



def slowText(text,amtime):

    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(amtime)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.5)
    print()

def getNumber(question,high,low):
    responce = None
    while responce not in range(low,high):
        slowText(question,0.03)
        responce = input()
        if responce.isnumeric():
            responce = int(responce)
        else:
             slowText("Please enter a number. I can't understand what you put in.",0.01)
    return responce

def shop (Ox, Food, Ammo, Clothes, Parts, Money):
    bill = 0
    ox = 0
    food = 0
    ammo = 0
    clothes = 0
    parts = []
    items = ["Oxen","Food", "Ammunition", "Clothes", "Wagon Parts", "Check Out"]
    spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
    slowText(" Before leaving Independance you should buy items",0.02)
    slowText(str.format("You have {} in cash to make the trip",money),0.02)
    slowText("remember you can buy supplies along the way",0.03)
    slowText("Press Enter to Continue",0.03)
    input()

    while True:
        spent_on_items[len(spent_on_items)-1] = bill
        slowText("Welcome to the Trail Store",0.03)
        slowText("Here is a list of things you can buy",0.03)
        slowText("Push 7 to clear.", 0.03)
        for i in range (len(items)):
            slowText(str.format("{}.        {:20}     ${:.2f}",i+1,items[i],spent_on_items[i]),0.02)
        slowText(str.format("Total Bill so far:       ${:.2f}",bill),0.03)
        slowText(str.format("Total Funds available:   ${:.2f}",money-bill),0.03)
        choice = getNumber("What Item would you like to buy?",8,1)# make sure this is a call to your number function
        if choice == 1:
            bill -= spent_on_items[0]
            ox = 0
            spent_on_items[0] = 0.00
            slowText("""
            There are 2 oxen in a yoke;
            I recomend at least 3 yokes.
            I charge $40 a yoke""",0.03)
            slowText(str.format("Total Bill so far:          ${:.2f}",bill),0.03)
            answer = int(input("How many yoke do you want"))
            cost = answer*40
            ox = answer*2
            bill += cost
            spent_on_items[0] = cost

        elif choice == 2:
            bill -= spent_on_items[1]
            food = 0
            spent_on_items[1] = 0.00
            slowText("""
            Rations are highly valuable;
            I recomend at least 100 rations a person.
            I charge $1 a ration""",0.03)
            slowText(str.format("Total Bill so far:          ${:.2f}",bill),0.03)
            answer = int(input("How many rations do you want"))
            cost = answer*1
            food = answer*1
            bill += cost
            spent_on_items[1] = cost


        elif choice == 3:
            bill -= spent_on_items[2]
            ammo = 0
            spent_on_items[2] = 0.00
            slowText("""
            ammo has 3 bullets per cartridge;
            I recomend at least 50 ammo cartridges.
            I charge $10 a cartridge""",0.03)
            slowText(str.format("Total Bill so far:          ${:.2f}",bill),0.03)
            answer = int(input("How many cartridges would you like"))
            cost = answer*10
            ammo = answer*3
            bill += cost
            spent_on_items[2] = cost

        elif choice == 4:
            bill -= spent_on_items[3]
            clothes = 0
            spent_on_items[3] = 0.00
            slowText("""
            Clothes come in packs of 2;
            I recomend at least 10 per person.
            I charge $15 a pack""",0.03)
            slowText(str.format("Total Bill so far:          ${:.2f}",bill),0.03)
            answer = int(input("How much clothes would you like"))
            cost = answer*15
            clothes = answer*2
            bill += cost
            spent_on_items[3] = cost

        elif choice == 5:
            slowText("""
            It is a good idea to have a few
            Spare parts for your wagon on hand
            you never know what can happen on
            the trail and a broken down
            wagon can be a death sentance""",0.03)
            parts_bill = 0.00
            partTotal = 0.00
            indPartBill = [0.00, 0.00, 0.00, parts_bill]
            parts = ["Wagon Wheel", "Wagon axle", "Wagon Tongue", "Checkout"]
            parts_cost =[10.00,20.00,50.00,parts_bill]
            while True:
                parts_cost[len(parts_cost)-1] = parts_bill
                slowText("Here is a list of things you can buy",0.03)
                for i in range(len(parts)):
                    slowText(str.format("{}.        {:20}     ${:.2f}",i+1,parts[i],indPartBill[i]),0.03)
                slowText(str.format("Total Bill so far:       ${:.2f}",partTotal),0.03)
                slowText(str.format("Total funds available   ${:.2f}",money-bill-partTotal),0.03)
                item = int(input("What Item would you like to buy"))
                if item == 1:
                    answer = int(input("How many wagon Wheels do you want?"))
                    for i in range(answer):
                        inventory.append("Wagon Wheel")
                    parts_bill += parts_cost[0]*answer
                    indPartBill[0] = parts_cost[0]*answer
                    cost = parts_cost[0]*answer
                    partTotal += cost
                elif item == 2:
                    answer = int(input("How many wagon Axles do you want?"))
                    for i in range(answer):
                        inventory.append("Wagon Axle")
                    parts_bill += parts_cost[1]*answer
                    indPartBill[1] = parts_cost[1]*answer
                    cost = parts_cost[1]*answer
                    partTotal += cost
                elif item == 3:
                    answer = int(input("How many wagon Tongues do you want?"))
                    for i in range(answer):
                        inventory.append("Wagon Tongue")
                    parts_bill += parts_cost[2]*answer
                    indPartBill[2] = parts_cost[2]*answer
                    cost = parts_cost[2]*answer
                    partTotal += cost
                elif item == 4:
                    bill += parts_bill
                    spent_on_items[4] = parts_bill
                    break
        if choice == 6:
            if bill <= money:
                money <= money
                return money, food, ammo, clothes, parts, ox
            else:
                slowText("You dont have that much money alter your shopping list",0.03)

        if choice == 7:
            shop(ox, food, ammo, clothes, parts, money)



money = 1000
food = 0
ammo = 0
clothes = 0
parts = []
ox = 0
inventory = []
shop(money, food, ammo, clothes, parts, ox)
