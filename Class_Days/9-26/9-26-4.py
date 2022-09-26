#[20,34,23,2,11,24,4,20,21,12,20,20,20] without 20

numbers  = [20,34,23,2,11,24,4,20,21,12,20,20,20]

clean = []

for n in numbers:
    if n != 20:
        clean.append(n)
        #variable #appened makes it in a list
print(numbers)
print(clean)

