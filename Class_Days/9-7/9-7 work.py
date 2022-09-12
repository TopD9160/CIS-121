### script that asks for income, if income is greater then 4,500,000 day "Damn u rich", if less say "you got it"

income = int(input("what is your income?"))

if income > 4500000 : #prints if more then amount
    print("Damn u rich")

elif income < 4500000 : #prints if less the  amount# ##elif and else do the same thing, no need for elif as there is nothing else, but both work
    print("you got it")
