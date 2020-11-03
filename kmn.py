import time
import sys

def get_number(question,high,low):
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

def endgame():
    yesno = input("Do you want to quit?\n")
    if yesno == "yes":
        slowText("You chose to win. Okay, you won.",0.03)
        input()
        quit()
    else:
        slowText("Mmmmmmmmmmmmmmmkay then.",0.01)


def makelogo():
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


makelogo()
numbie = get_number("Choose 1 please.",2,1)
if numbie == 1:
    endgame()
makelogo()
