# 1
    # A: No, your asking for a name and random number but isnt used for anything. If it had a print using name, age, and number it would work
    # B: No, you need a input. Otherwise the script wont function at the number variable has no number
    # C: Yes, it works
    # D: Yes, it works
        #for i in range(1,10):
            #print(i)
    #E: No, as any number entered the script will ask for a input again, even 5.
        #user_number = 0
        # while user_number != 5:
        #user_number = input("enter number")

#### 2 

#milk = int(input("Amount of cartons of milk: "))
#eggs = int(input("Amount of eggs: "))
#bacon = int(input("Amount of bacon: "))

#total = (milk * 2.00) + (eggs * 1.50) + (bacon * 3.00) #takes amounts and prices
#tax = total * .11 #taxes
#total_with_taxes = total + tax #adds taxes to total

#print("Items: ", milk, "milk,", eggs, "eggs, and", bacon, "bacon. Total before taxes is", "$"+str(total)) #amount of items and price before taxes
#print("Total is","$"+str(total_with_taxes), "(taxes included)") #after taxes

##### 3
#number = input("Enter phone number: ")

#needs to be like (777) 555-4323
#print("("+str(number[0:3])," ", (number[3:6]),"- "+str(number[6:10])) ###### idk feels like you need to use str but maybe im wrong. dont know how to get rid of the space after the second 3 and get a ) after the first 3

##### 4

for number in range(0,61): #takes numbers
    if number % 2 == 0: and # prints if even
        print(number)


if number % 2 == 0 and number >= 15 : #if even and greater then 15
    print("I generated the number", number,", randomly")