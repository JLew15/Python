import time
import sys

def slowText(text,amtime):
    for char in text:
        time.sleep(amtime)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.5)
    print()


money = 1000
slowText(str.format("You have {} in cash to make the trip",money),0.02)
