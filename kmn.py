import time
import sys
import datetime
import random

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


def checkSupplies(ox,food,ammo,clothes,parts,money):
    slowText("You have " + str(ox) + " oxen",0.03)
    slowText("You have " + str(food) + " rations",0.03)
    slowText("You have " + str(ammo) + " cartridges",0.03)
    slowText("You have " + str(clothes) + " clothes",0.03)
    slowText("You have " + str(money) + " money",0.03)












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


def turn(health,weather,rations,healthCondition,food,currentDate,ox,members):
    weather = random.choice(["hot","good","fair","poor","windy","rain","blizzard"])

    #Sets Health Condition based on amount of Health
    if health >= 80:
        healthCondition = "good"
    elif health < 80 and health >= 50:
        healthCondition = "fair"
    else:
        healthCondition = "poor"


    #Sets ration modifier based on what ration setting you are on.
    if rations == "full":
        rationsModifier = 2
    elif rations == "half":
        rationsModifier = 1
    else:
        rationsModifier = 0.5

    problem = random.choice(["lost","snake bite","sick","ox died","none","none","none","none","none","none","none","none","none","none"])

    if problem == "lost":
        lost = random.randint(1,7)
        print("One of your members got lost for",lost,"days")
        currentDate += datetime.timedelta(days = lost)
        food -= members*rationsModifier*lost
    elif problem == "snake bite":
        health -= 50
    elif problem == "sick":
        health -= 20
    elif problem == "ox died":
        ox -= 1
        food += 50
    else:
        pass

    print(str.format("""
   .....                                        ..'..                              ..',,,'..
..',;;;,,'...  ...                       ..'''',,;;;;,..                       ..',;;;;;;;;,,,'..
,;;,;;;;;,;;;,,,;,,...               ..',;;;;;,,;;;;;;;;,'..     ..''....',,'',,;;;;;;;;;;,;;;;;,'..
;;;;;;;;;;;;;;;;;;;;;,,....'..   ..',;;;;;;;;;;;;;;;;;;;;;;,'..',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,',,;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
''''''''''''''',,,''''.........'''''',,,''''''''''''',,;;;;;,,,,,,,,,,,,;;;;;;;;;;;;,,,''...'',,,;;;
                                                      ........        ...............            ...
 +-----------------------------+
 |Date:{:_>24}|
 |Weather:{:_>21}|           ..'''''''''''..                         ..''''''.
 |Health:{:_>22}|          ,:ccccllllllllc::::,...  ......  ..,::::::clclllcc,.
 |Miles Travled:{:_>15}|         .cc'.;cccclccccccccclc'.;cllllc;.'ccccccccccccclcl;.
 |Miles To Go:{:_>17}|          .;c, .,:clcclclcclcclc'.clcccclc.'cccccccccccclll:.
 |Food:{:_>24}|           .cc.  .';cccclcclcclc'.clcccclc.'cccccccccccccc:.
 +-----------------------------+            ,:;.   'ccccccclcclc'.clcccclc.'cccccccccccccc'
                 ..                         .;c;.   ,ccclccccllc'.clcccllc.'cccccclccllcc,
          .,,. .'::.  ....                   .:c.   .clcccccclcc'.cccccclc.'cccccccccccc'
           .,:::cl,..',';c;:;;;;:;;;'.        ',.   .:cccccccccc..:cccccc:.'ccccccccccc:.
         .';clcccl,';;::ccccccccccccc:.       ....  ......,,,,'.  .............',,,,..','.
          ...';:;,,;cccllcclcclccccccc........'.''.',...',.,;',,. .,','',,,  .,'';,','.''.
                .;:clcclcccclllccccc:,.      ...',... .,'. ', .';. ..,',,.. .;. .,. .,,.
                 .'clcccc::;'.,:lclc.         ..''    ';...;;...;'   ''''   ,;..';,..';.
                  .cc,:c;..  .,cc,:c.                 .,'. ', .',.          .;. .,. .,,.
                .':c,..;l'   .';:;:c.                  .',',;','.            .,,';,',.
'..''.''''.'''.',:c:,'';:,''''',::::,'''''...'''''''''''',;;;;,''''''''''..'''';;;;;,'''.''''''''''.
;;;;;;;;;;;;;;,;;:::;;;::;,,;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;,;::::;;;:;;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;,;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
;;;;;;;;;;;;;;;;;:::;;;::;;;;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;""",currentDate.strftime("%A %b, %d, %Y"),weather,health,milesTraveled,totalMiles,food))
    input()

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

def changeRations(rations):
    print ("your current Rations are", rations)
    options = ["full","half","quarter"]
    index = 1
    for option in options:
        print(str.format("{}     {}",index,option))
        index+=1
    while True:
        try:
            choice = int(input("choose your pace"))
            if choice == 1:
                return "full"
            elif choice == 2:
                return "half"
            elif choice == 3:
                return "quarter"
            else:
                print("not an option")
        except:
            print ("not a good input")

def changePace(pace):
    print ("your current pace is", pace)
    options = ["slow","normal","fast"]
    index = 1
    for option in options:
        print(str.format("{}     {}",index,option))
        index+=1
    while True:
        try:
            choice = int(input("choose your pace"))
            if choice == 1:
                return "slow"
            elif choice == 2:
                return "normal"
            elif choice == 3:
                return "fast"
            else:
                print("not an option")
        except:
            print ("not a good input")

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

money = 0
food = 0
ammo = 0
clothes = 0
parts = []
ox = 0
inventory = []
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
    name = getName()
    members = getNumber("How many members are in your family?",11,2)
    shop(ox, food, ammo, clothes, parts, money)
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    checkSupplies(ox,food,ammo,clothes,parts,money)

elif numbie == 2:
    learnTrail()

else:
    endGame()

makeLogo()
