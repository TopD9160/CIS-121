name = input("What if your name?")
income = int(input("how much do you make?"))

print("Hey", name, "You make" , income, "a year!")
print("This is how much money you will make in 20 years")

done = False
years = 1
money = 0

while done != True : 
    money = income*years
    print("$"+str(money*years),"Year",years)

    years +=1

    if years >= 10000 : 
        done = True