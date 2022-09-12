#create a guessing game. give the user 3 changes. If they get it right print("yay"), if not print a custom message
chances = 0
win = 0
num =4

while chances < 3 and win !=1:
    user = int(input("Please guess a number between 1-10. If wrong you lose a guess. You have 3 guesses"))


if user == num :
    print("yay!")
    win = 1

else: 
    chances += 1
    print("you are not correct. You have",chances,"guesses")