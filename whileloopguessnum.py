import random

theNumber = random.randint(1,10)

win = False
attempts = 1
maxAttempts = 3
maxNumber = 10

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and",maxNumber)
print("Try to guess it in",maxAttempts + " attempts.\n")

while attempts <= maxAttempts:
    if not win:

        guess = int(input("Pick a number between 1 and",maxNumber))

        if guess == theNumber:
            print("You win")
            win = True
            attempts = maxAttempts + 1
        elif guess > theNumber:
            print("Guess lower...")
            attempts = attempts + 1
        else:
            print("Guess higher...")
            attempts = attempts + 1

if win == False:
    print("You lose... the number was",theNumber)
