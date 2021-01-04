import time
import sys


def slowText(text, amtime):
    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(amtime)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.5)
    print()


def getNumber(question, high, low):
    response = None
    while response not in range(low, high):
        slowText(question, 0.03)
        response = input()
        if response.isnumeric():
            response = int(response)
        else:
            slowText("Please enter a number. I can't understand what you put in.", 0.01)
    return response


def yesNo(question):
    """Ask a question and receive yes or no"""
    response = None
    while response not in ("y", "n", "no", "yes"):
        response = input(question).lower()
    return response

def getName():
    while True:
        slowText("Please enter a name.", 0.02)
        response = input()
        if len(response) > 1:
            return response
        else:
            continue


class Player(object):
    def __int__(self, name, score=0):
        self.name = name
        self.score = score
        self.lives = 3


if __name__ = "__main__":
