import random

# Setting up variables
guessnum = 0
answer = 92410
variable1 = "TNTPop"

#Printing Welcome message
print("Welcome to the Guessing Game!")
print("Try and Guess my Number!")

# Starting a while loop that continues until the user enters an empty string as the guess
while True:
    guess = input("Guess: ")
    #Checking if the user's input is empty
    if guess == "":
        break
    #Checking if the user's input matches the variable1
    elif guess == variable1:
        print("Found the backdoor hey?, the answer is my birthday.")
    #Checking if the user's input is greater than the answer
    elif int(guess) > answer:
        print("Lower!")
        guessnum += 1
    #Checking if the user's input is less than the answer
    elif int(guess) < answer:
        print("Higher!")
        guessnum += 1
    #Checking if the user's input is the answer
    elif int(guess) == answer:
        print("Congratulations, You guessed right!!!\nIt took you", guessnum, "guesses.")
        break

