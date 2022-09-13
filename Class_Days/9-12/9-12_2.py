

##this does evens till 100


number = int(input("Type a number between 35-1000: "))

if 35 <= number <= 1000 :
    if number >= 100 :
        print("100")
    else : 
        while number <= 100:
            if number % 2 == 0 : #change occurs here
                print(number)
            number += 1
else :
    print("You did not enter a valid number")