#create script asking user for name, age, and number. add those values to a list and display them


name = input("what is your name? ")
age = float(input("what is your age? "))
number = int(input("what is your number? "))

info = [name,age,number]

print("name: ",info[0])
print("age: ",info[1])
print("number: ",info[2])