import random

maxNumber = 10

theNumber = random.randint(1,maxNumber)

win = False

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and",maxNumber)
print("Try to guess it in 3 attempts.\n")

if not win:

    guess = int(input("Pick a number between 1 and",maxNumber + " "))

    if guess == theNumber:
        print("You win")
        win = True
    elif guess > theNumber:
        print("Guess lower...")
    else:
        print("Guess higher...")

if not win:

    guess = int(input("Pick a number between 1 and",maxNumber + " "))

    if guess == theNumber:
        print("You win.")
        win = True
    elif guess > theNumber:
        print("Guess lower...")
    else:
        print("Guess higher...")

if not win:

    guess = int(input("Pick a number between 1 and",maxNumber + " "))

    if guess == theNumber:
        print("You win.")
        win = True
    elif guess > theNumber:
        print("You lost...")
        print("The number was...",theNumber)
    else:
        print("You lost...")
        print("The number was...",theNumber)
