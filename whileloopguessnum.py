import random



win = False
attempts = 1
maxAttempts = 3
maxNumber = 10
diff = 1

difficulty = input("Choose a difficulty... Easy, Medium, or Hard. ")

if difficulty == "Easy" or difficulty.startswith("E") or difficulty.startswith("e"):
    maxAttempts = 3
    maxNumber = 10
    diff = 1

elif difficulty == "Medium" or difficulty.startswith("M") or difficulty.startswith("m"):
    maxAttempts = 5
    maxNumber = 50
    diff = 2

else:
    maxAttempts = 10
    maxNumber = 100
    diff = 3

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and",maxNumber)
print("Try to guess it in", maxAttempts, " attempts.\n")

theNumber = random.randint(1,maxNumber)

while attempts <= maxAttempts:
    if not win:

        guess = int(input("Pick a number between 1 and " + str(maxNumber)))

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
