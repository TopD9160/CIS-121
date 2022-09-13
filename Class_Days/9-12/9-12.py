#write small script asking the user for a number between 35-1000, when user enters the number your program should print the numbers that x number to 100
#ex if person tpes 35, it will count all the way to 100
#if mumber goes above 100 print the 100 its self 

number = int(input("Type a number between 35-1000: "))

if 35 <= number <= 1000 :
    if number >= 100 :
        print("100")
    else : 
        while number <= 100:
            print(number)
            number += 1
else :
    print("You did not enter a valid number")



#boolean
 winner = True
loser = False 