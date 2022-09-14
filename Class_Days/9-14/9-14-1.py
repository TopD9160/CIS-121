#   write a script that keeps asking the user for a number and check if the number is even or odd.
#  Let the user know what it is. If they enter the number 0 stop asking

done = False

while done != True : 
    number = int(input("Please type a number "))

    if number == 0 :
      print("bye")
      done = True
    elif number % 2 == 0 :
        print("Even")
    else :
        print("Odd") 