import random
HANGMAN = """


--------
|---|
|  ( )
|
|
|
|
|
|
--------

--------
|---|
|  ( )
|   +
|   +
|   +
|
|
--------

--------
|---|
|  ( )
|   +-\\
|   +
|   +
|
|
--------

--------
|---|
|  ( )
| /-+-\\
|   +
|   +
|
|
--------

--------
|---|
|  ( )
| /-+-\\
|   +
|   +|
|    |
|
--------

--------
|---|
|  ( )
| /-+-\\
|   +
|  |+|
|  | |
|
--------
"""




MAX_WRONG = len(HANGMAN)-1
WORDS = ("ANNOTATION","BINARY","FUNCTION","IDLE","MODULE","OBJECT","SLICE","TYPE","BYTECODE","DESCRIBER")

# option 1
##word_index=random.randint(o,len(WORDS))
##word = WORDS[word_index]
##print(word_index)
##option 2
word = random.choice(WORDS)
so_far = "_"*len(word)
used = []
wrong = 0
guess = ""


print("welcome to Hangman. Good Luck!")


while wrong< MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print()
    print("\nSo far, the world is:\n",so_far)

    print("\nYou've used the following letters:\n", used)

    while guess in used:
        guess = input("\n\nEnter your guess: ")
        guess = guess.upper()
        print(guess)

    used.append(guess)

    if guess in word:
        print("\nYes!", guess, "is in the word!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new+=guess
            else:
                new+=so_far[i]
            so_far = new
        else:
            print("\nSorry,",guess,"isn't in the word.")
            wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hagned!")
    print("\nSo far, the word is:\n",so_far)
else:
    print(HANGMAN[wrong])
    print("\nYpu guessed it!")
    print("\nThe word was:\n",so_far)

input("\n\nPress the enter key to exit.")
