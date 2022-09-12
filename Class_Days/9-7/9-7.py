number = 1

if number == 10:
    print("this is 10")

elif number > 10 : #prints if its more than 10
    print("this is more then ten")
    print("interesting")

elif number < 10 : #prints if above is not met (any number less then 10)
    print("wow this is crazy its less then 10")

else:  #prints if the above does not meet criteria
    print("what are you doing this does not make sense")

while number <= 10 or number == 50: #( can use "or" and "and" if needed) #every number less then 10 is printed as well as meeting the criteria below, mutiple while can happen at the same time
    print(number)
    number = number + 1