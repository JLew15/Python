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
    slowText("Banker: Starts with $600",0.03)
    slowText("Carpenter: Starts with $400",0.03)
    slowText("Farmer: Starts with $200",0.03)
    slowText("""0$ H┴IM S┴ɹ∀┴S :ɹƎɹƎpɹ∩W""",0.03)

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
slowText("Push 1 to play",0.03)
slowText("Push 2 to learn", 0.03)
numbie = getNumber("Push 3 to win",4,1)

if numbie == 1:
    characters()

elif numbie == 2:
    learnTrail()

else:
    endGame()

makeLogo()
