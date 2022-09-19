#asking user for their age. Then use that value to print out the next 20 years (use a FOR loop)
def askForAge():
    age = int(input("Please enter your age: "))
    return age
age = askForAge()

for age in range(age,age + 21):
    print(age)