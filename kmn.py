import time
import sys

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


def slowText(text,amtime):

    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(amtime)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.5)
    print()

def endGame():
    yesno = input("Do you want to quit?\n")
    if yesno == "yes":
        slowText("You chose to win. Okay, you won.",0.03)
        input()
        quit()
    else:
        slowText("Mmmmmmmmmmmmmmmkay then.",0.01)

def learnTrail():
    slowText("You will be transversing 2,000 miles across the plains and mountains\
. You will travel on covered wagons with oxen through heavy terrain.",0.02)
    input()
    slowText("Crossing rivers will be tricky with the option to either by a ferry\
 float across or have the oxen pull through the rivers.",0.02)
    input()
    slowText("If you are low on food you can hunt and get your rations back up",0.02)
    input()
    slowText("There will be choices between navigating rivers rapids or taking\
 the long way by transversing land, choose wisely.",0.02)
    input()
    slowText("Never give up and try over and over till you win and then go for\
 fastest trailer!",0.02)
    input()
    slowText("The absolute best #1 Lads of the land and sky AKA the develepers\
 are Ethan (absolute lad) Eash and Jaiden (The man and a half) Lewis",0.2)
    input()

def characters():
    slowText("1)Banker: Starts with $600",0.03)
    slowText("2)Carpenter: Starts with $400",0.03)
    slowText("3)Farmer: Starts with $200",0.03)
    slowText("""4)0$ H┴IM S┴ɹ∀┴S :ɹƎɹƎpɹ∩W""",0.03)
    characterChoice = getNumber("Choose your character...",5,1)
    if characterChoice == 1:
        character = "Banker"
        money = 600
        slowText("You have chose to be a Banker. Are you sure of your answer?",0.03)
        returnChoice = getNumber("Choose 1 for yes, Choose 2 for no.",3,1)
        if returnChoice == 2:
            money = 0
            characters()
        else:
            screech = 1
            return screech
    elif characterChoice == 2:
        character = "Carpenter"
        money = 400
        slowText("You have chose to be a Carpenter. Are you sure of your answer?",0.03)
        returnChoice = getNumber("Choose 1 for yes, Choose 2 for no.",3,1)
        if returnChoice == 2:
            money = 0
            characters()
        else:
            screech = 2
            return screech
    elif characterChoice == 3:
        character = "Farmer"
        money = 200
        slowText("You have chose to be a Farmer. Are you sure of your answer?",0.03)
        returnChoice = getNumber("Choose 1 for yes, Choose 2 for no.",3,1)
        if returnChoice == 2:
            money = 0
            characters()
        else:
            screech = 3
            return screech
    else:
        character = "Murderer"
        money = 0
        slowText("YOU ARE A MURDERER. Are you sure?",0.06)
        returnChoice = getNumber("Choose 1 for yes, Choose 2 for no",3,1)
        if returnChoice == 2:
            money = 0
            characters()
        else:
            screech = 4
            return screech


def getName():
    while True:
        slowText("Please enter a name.",0.02)
        response = input()
        if len(response) > 1:
            return response
        else:
            continue



def shop (Ox, Food, Ammo, Clothes, Parts, Money):
    bill = 0
    items = ["Oxen", "Ammunition", "Wagon parts", "Check Out"]
    spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
    print(" Before leaving Independance you should buy items")
    print(str.format("You have {} in cash to make the trip",money))
    print("remember you can buy supplies along the way")
    input("Press Enter to Continue")

    while True:
        spent_on_items[len(spent_on_items)-1] = bill
        print("Welcome to the BigDumbStupid Store")
        print("Here is a list of things you can buy")
        for i in range (len(items)):
            print(str.format("{}.        {:20}     ${:.2f}",i+1,items[i],spent_on_items[i]))
        print(str.format("Total Bill so far:       ${:.2f}",bill))
        print(str.format("Total Funds available:       ${:.2f}",money-bill))
        input()
        choice = getNumber("What Item would you like to buy?")# make sure this is a call to your number function
        if choice == 1:
            bill -= spent_on_items[0]
            ox = 0
            spent_on_items[0] = 0.00
            Print("""
            There are 2 oxen in a toke;
            I recomend at least 3 yokes.
            I charge $40 a toke""")
            print(str.format("Total Bill so far:          ${:.2f",bill)
            answer = int(input("How many yoke do you want"))
            cost = answer*40
            ox = answer*2
            bill += cost
            spent_on_items{0} = cost

        elif choice == 2:
            bill -= spent_on_items[0]
            food = 0
            spent_on_items[0] = 0.00
            Print("""
            Rations are highly valuable;
            I recomend at least 100 rations a person.
            I charge $1 a ration""")
            print(str.format("Total Bill so far:          ${:.2f",bill)
            answer = int(input("How many rations do you want"))
            cost = answer*1
            rations = answer*1
            bill += cost
            spent_on_items{0} = cost


        elif choice == 3:
            bill -= spent_on_items[0]
            ammo = 0
            spent_on_items[0] = 0.00
            Print("""
            ammo has 3 bullets per cartridge;
            I recomend at least 50 ammo cartridges.
            I charge $10 a cartridge""")
            print(str.format("Total Bill so far:          ${:.2f",bill)
            answer = int(input("How many cartridges would you like"))
            cost = answer*10
            ammo = answer*3
            bill += cost
            spent_on_items{0} = cost

        elif choice == 4:
            bill -= spent_on_items[0]
            clothes = 0
            spent_on_items[0] = 0.00
            Print("""
            Clothes come in packs of 2;
            I recomend at least 10 per person.
            I charge $15 a pack""")
            print(str.format("Total Bill so far:          ${:.2f",bill)
            answer = int(input("How much clothes would you like"))
            cost = answer*15
            ammo = answer*2code15
            bill += cost
            spent_on_items{0} = cost

        if choice == 5:
                  print("""
            It is a good idea to have a few
            Spare parts for your wagon on hand
            you never know what can happen on
            the trail and a broken down
            wagon can be a death sentance""")
            pars_bill = 0.00
            parts = ["Wagon Wheel", "Wagon axle", "Wagon Tongue"]
                  parts_cost =[10.00,20.00,50.00,parts_bill]
            while True:
                parts_cost[len(parts_cost)-1] = parts_bill
            print("Here is a list of things you can buy")
            for i in range(len(parts)):
                print(str.format("Total Bill so far:      ${:.2f}",bill))
            print(str.format("Total funds available   ${:.2f}",money))
            item = int(input("What Item would you like to buy"))
            if item == 1:
                answer = int(input("How many wagon Wheels do you want?"))
                for i in range(answer):
                    inventory.append("Wagon Wheel")
                parts_bill += parts_cost[0]*answer
            elif item == 2:
                answer = int(input("How many wagon Axles do you want?"))
                for i in range(answer):
                    inventory.append("Wagon Axle")
                parts_bill += parts_cost[1]*answer
            elif item == 3:
                answer = int(input("How many wagon Tongues do you want?"))
                for i in range(answer):
                    inventory.append("Wagon Tongue")
                parts_bill += parts_cost[2]*answer
            elif item == 4:
                bill += parts_bill
                spent_on_items[4] = parts_bill
                break





money = 1000
food = 0
ammo = 0
clothes = 0
parts = []
ox = 0
shop(money, food, ammo, clothes, parts, ox)






def makeLogo():
    slowText("""

\t\tYYYYYYY       YYYYYYY               AAA                    BBBBBBBBBBBBBBBBB
\t\tY:::::Y       Y:::::Y              A:::A                   B::::::::::::::::B
\t\tY:::::Y       Y:::::Y             A:::::A                  B::::::BBBBBB:::::B
\t\tY::::::Y     Y::::::Y            A:::::::A                 BB:::::B     B:::::B
\t\tYYY:::::Y   Y:::::YYY           A:::::::::A                  B::::B     B:::::B
\t\t   Y:::::Y Y:::::Y             A:::::A:::::A                 B::::B     B:::::B
\t\t    Y:::::Y:::::Y             A:::::A A:::::A                B::::BBBBBB:::::B
\t\t     Y:::::::::Y             A:::::A   A:::::A               B:::::::::::::BB
\t\t      Y:::::::Y             A:::::A     A:::::A              B::::BBBBBB:::::B
\t\t       Y:::::Y             A:::::AAAAAAAAA:::::A             B::::B     B:::::B
\t\t       Y:::::Y            A:::::::::::::::::::::A            B::::B     B:::::B
\t\t       Y:::::Y           A:::::AAAAAAAAAAAAA:::::A           B::::B     B:::::B
\t\t       Y:::::Y          A:::::A             A:::::A        BB:::::BBBBBB::::::B
\t\t    YYYY:::::YYYY      A:::::A               A:::::A       B:::::::::::::::::B
\t\t    Y:::::::::::Y     A:::::A                 A:::::A      B::::::::::::::::B
\t\t    YYYYYYYYYYYYY    AAAAAAA                   AAAAAAA     BBBBBBBBBBBBBBBBB
""",0.01)




    slowText("\n\n\n\n\t\t\t\t\tCOPYRIGHT of YAB Co. (C) 2020",0.1)


makeLogo()
numbie = getNumber("""Push 1 to play
Push 2 to learn
Push 3 to win""",4,1)

if numbie == 1:
    screech = characters()
    if screech == 1:
        character = "Banker"
        money = 600
    elif screech == 2:
        character = "Carpenter"
        money = 400
    elif screech == 3:
        character = "Farmer"
        money = 200
    else:
        character = "Murderer"
        money = 0
    print(character)
    print(money)
    name = getName()
    slowText(name, 0.01)
    test = getNumber("How many members are in your family?",11,2)
    print(test)

elif numbie == 2:
    learnTrail()

else:
    endGame()

makeLogo()
