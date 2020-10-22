#Orange - Caleb Keller
#Jaiden - Blue
#Green - Jadiah
#Pink  - Jack
import time
import sys

def getResponse(question,options,i):
    """!!!MAKE SURE TO INCLUDE INDEX AT END!!!
    INDEX IS USED TO HELP TRACK BAD CHOICES
    GETS RESPONSE FROM DECISION AND MAKES SURE IT IS VALID"""

    badInputFile = open("BADINPUTS.txt", "a")

    badResponse = ["That's an invalid choice... try again please. ",,
     "Come on man, you know that won't work. Try again.",
     "Think about that answer for a second... do you think it would actually work? Try again..."]

    count = 0
    while True:

        slowText(question)

        response = input().upper()
        if response in options:
            badInputFile.close()
            return response

        else:
            badInputFile.write(i +" " + response + "\n")
            x = random.choice(badResponse)
            slowText(x)
            badResponse.remove(x)
            count += 1

        if not badResponse:
            kill()
def get_number(question,high,low):
    responce = None
    while responce not in range(low,high):
        slowText(question)
        responce = input()
        if responce.isnumeric():
            responce = int(responce)
        else:
             slowText("Please enter a number. I can't understand what you put in.")
    return responce
def slowText(text):

    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.5)
    print()

def kill():
    """KILLS OFF PLAYER AND RESTARTS PROGRAM"""
    slowText("\nDude... you really must be stupid.. You died. Start over.")
    input()
    main()

def pop_inv(num, item, inventory):
    xnum = num
    while xnum != 0:
        while len(inventory) < 10:
            for i in range (xnum):
                if len(inventory) < 10:
                    inventory.append(item)
                    xnum = xnum -1
            break
        else:
            slowText("You are carrying too many items...")
            drop(inventory)
            continue

def drop(inventory):
    run = True
    while run:
        dropItem = getResponse("Would you like to drop some items?",["YES","NO","Y","N"],"Drop Inventory Question")
        if dropItem in ["YES","Y"]:
            print(inventory)
            item = getResponse("What item do you want to drop?",inventory,"Drop Question 2")
            if item in inventory:
                inventory.remove(item)
            else:
                slowText("That is not in your inventory.")
        else:
            run = False

def main():
    """MAIN PROGRAM"""
    lit_candle = True
    inventory = []
    numBlow = 0

    #Story Variables
    awakening = "You awake within a dark cave..."
    cav_descrip = """\nThe ceiling is too high to see, darkness stretches in all \
directions and the only source of light is a circle of fifteen candles centered around \
your prone body."""
    darkness = """\nThe small circle of light is crushed by the oppressive darkness \
and you feel all warmth leave your body"""
    poltargeist = """\nBefore long, you begin to hear whispers echoing off the walls of the cavern. \
The voices start to draw nearer..."""
    flee = "\nYou turn opposite the whispers, and sprint forward. You feel the \
air rushing past your ears before... it doesn't. You run headlong into a very hard surface. \
Everything goes black... again."
    cower = "\nAny hope of putting up a fight or creating a diversion is lost to your mind. \
The terror is overwhelming. You crouch low in the hopes of being missed by \
whatever entity is causing the piercing whispers."
    deeper = "\nYou choose to go deeper into the blinding darkness."
    direction = "As the sound of grinding stone subsides, it dawns on you that \
you are in complete darkness once again."
    flee = "\nYou turn opposite the whispers, and sprint forward. You feel the \
air rushing past your ears before... it doesn't. You run headlong into a very hard surface. \
Everything goes black... again."
    cower = "\nAny hope of putting up a fight or creating a diversion is lost to your mind. \
The terror is overwhelming. You crouch low in the hopes of being missed by \
whatever entity is causing the piercing whispers."
    theUnderOasis = "You decide to dump out the moldy potatos and carry the candles in the sack \
while using one to light the deep cave"
    burnAlive = "Sad thing is, you forgot the candles were lit and you caught the sack on fire..."
    fight = "You try to put up a fight with whatever spirit you feel haunting you \
but your punches only hit air, nothing connects and you fall to the ground from \
exhaustion..."
    #Variables CHOICES
    choice1 = "\nYou have a choice between blowing out the candles, \
or journeying into the abyssal caverns:"
    choice2 = "\nWhat do you do?:"
    candleChoice = "Before you go deeper \
you have a choice of how many candles you will take none, one, half, or \
all of the candles:"
    one_candle = "\nWith your one candle, you find the cave branches off to the left and right. Where do you go?"
    secOneChoice = "You walk towards the left tunnel when you hear rocks start to tumble down \
from the side of the cave. Do you run down the left or the right"
    potatoes = "You see a sack of moldy potatoes just out of the candle light. do you take it?"
    candleBlow = "You chose to blow out your candles, how many do you want to blow out?"


#GAME LOGIC
    slowText(awakening)
    #waking up
    slowText(cav_descrip)
    #slowText(choice1)
    decision = getResponse(choice1,["BLOW", "CANDLE","PUT OUT", "PASS", "GO", "DEEPER", "EXPLORE", "MOVE"],"Journey Choice")
    #blowing choice
    if decision in ["BLOW", "CANDLE","PUT OUT"]:
        numBlow = get_number(candleBlow,16,1)
        if numBlow == 15:
            lit_candle = False

            slowText(darkness)

            slowText(poltargeist)

            decision2 = getResponse(choice2,["RUN","HIDE","CROUCH","FIGHT"], "Poltargeist Choice")
            if decision2 in ["RUN"]:
                    #flee choice
                    slowText(flee)
        #cower choice
            elif decision2 in ["HIDE","CROUCH"]:
                slowText(cower)
        #fight choice
            elif decision2 in ["FIGHT"]:
                slowText(fight)
            #deeper choice
        elif  numBlow<15:
            decision = "PASS"
    if decision in ["PASS", "GO", "DEEPER", "EXPLORE", "MOVE"]:
        slowText(deeper)
        candle_num = get_number(candleChoice,16,1)
        pop_inv(candle_num,"CANDLE",inventory)
        if candle_num == 1 and lit_candle:
    #one candle choice
            walking_one_candle = getResponse(one_candle,["LEFT", "RIGHT", "R", "L"], "Direction Choice One Candle")
            if walking_one_candle in ["LEFT", "RIGHT", "L", "R"]:
                thepassage = getResponse(secOneChoice,["R", "RIGHT", "L", "LEFT"], "Second Direction Choice One Candle")
                if thepassage in ["R", "RIGHT", "L", "LEFT"]:
                    slowText(direction)

                slowText(poltargeist)

                decision2 = getResponse(choice2,["RUN", "HIDE","CROUCH","FIGHT"], "Poltargeist Choice")
                if decision2 in ["RUN"]:

                        slowText(flee)

                elif decision2 in ["HIDE","CROUCH"]:

                    slowText(cower)

                elif decision2 in ["FIGHT"]:
                    slowText(fight)

        elif candle_num>1 and numBlow>= 14:
            travelingDeeper = getResponse(potatoes,["YES", "NO", "Y", "N"],"Potato Choice")
            if travelingDeeper in ["YES"]:
                slowText(theUnderOasis)
        elif candle_num > 1:
            travelingDeeper = getResponse(potatoes,["YES", "NO", "Y", "N"],"Potato Choice")
            if travelingDeeper in ["YES"]:
                slowText(theUnderOasis)
                slowText(burnAlive)
                kill()



















main()
