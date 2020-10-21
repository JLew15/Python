#ORANGE - Caleb Keller
#Jaiden - Blue
#Green - Jadiah
#Pink  - Jack
#Who put this down?:
##print("you hear of a haunted cave and are wishing to have a good scare, a ghost hits a rock against your head and then another posseses you while your in a coma.")
import random
import time
import sys

def getResponse(question,options,i):
    """!!!MAKE SURE TO INCLUDE INDEX AT END!!!
    INDEX IS USED TO HELP TRACK BAD CHOICES
    GETS RESPONSE FROM DECISION AND MAKES SURE IT IS VALID"""

    badInputFile = open("BADINPUTS.txt", "a")

    badResponse = ["That's an invalid choice... try again please. ",
     "You're really an idiot, aren't you? Try again...",
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

def main():
    """MAIN PROGRAM"""
    #Story Variables
    awakening = "You awake within a dark cave..."
    cav_descrip = """\nThe ceiling is too high to see, darkness stretches in all \
directions and the only source of light is a circle of candles centered around \
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
    theunderoasys = "You decide to dump out the moldy potatos and carry the candles in the sack \
while using one to light the deep cave"
    burnalive = "Sad thing is, you forgot the candles were lit and you caught the sack on fire..."

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


#GAME LOGIC
    slowText(awakening)
    #waking up
    slowText(cav_descrip)
    #slowText(choice1)
    decision = getResponse(choice1,["BLOW", "CANDLE","PUT OUT", "PASS", "GO", "DEEPER", "EXPLORE", "MOVE"],"Journey Choice")
    #blowing choice
    if decision in ["BLOW", "CANDLE","PUT OUT"]:
        slowText(darkness)

        slowText(poltargeist)

        decision2 = getResponse(choice2,["RUN"], "Poltargeist Choice")
        if decision2 in ["RUN"]:
                #flee choice
                slowText(flee)
    #cower choice
        else:
            slowText(cower)
        #deeper choice
    elif decision in ["PASS", "GO", "DEEPER", "EXPLORE", "MOVE"]:
        slowText(deeper)
        candle_num = getResponse(candleChoice,["NONE","ZERO","0","ONE", "HALF", "ALL","1"], "Candle Choice")
        if candle_num in ["ONE","1"]:
    #one candle choice
            walking_one_candle = getResponse(one_candle,["LEFT", "RIGHT", "R", "L"], "Direction Choice One Candle")
            if walking_one_candle in ["LEFT", "RIGHT", "L", "R"]:
                thepassage = getResponse(secOneChoice,["R", "RIGHT", "L", "LEFT"], "Second Direction Choice One Candle")
                if thepassage in ["R", "RIGHT", "L", "LEFT"]:
                    slowText(direction)

                slowText(poltargeist)

                decision2 = getResponse(choice2,["RUN"], "Poltargeist Choice")
                if decision2 in ["RUN"]:
                        #make him run into the wall of the cave ;P lol

                        slowText(flee)

                else:

                    slowText(cower)

        elif candle_num in ["HALF", "ALL"]:
            travelingdeeper = getResponse(potatoes,["YES", "NO", "Y", "N"],"Potato Choice")
            if ["YES"] in travelingdeeper:
                slowText(theunderoasys)
                slowText(burnalive)
                kill()


















main()
