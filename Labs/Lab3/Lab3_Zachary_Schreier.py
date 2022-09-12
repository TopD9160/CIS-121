"""
Zachary Schreier
9/8/22

This program takes the persons income and martial status to determine taxes owed
#if person has 20k single must do the 10% of the 9950 and the 12 of the 20k
"""
import sys


taxOwed = 0.0

earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
if earnedIncome < 0:
	print("You made less than $0. Contact an accountant")
	sys.exit()

print("Are you married or single?")
maritalStatus = input("Type m for married and s for single: ")


#Ensures you have a valid marital status
while maritalStatus != "m" and maritalStatus != "s":
	print("you entered an invalid marital status")
	maritalStatus = input("Type m for married and s for single: ")

#If the person is single
if  maritalStatus == "s" and earnedIncome <= 9950 : #Martial Status is single # first if for under 9950
	taxOwed = earnedIncome * .10
	print("You owe",taxOwed,"in taxes")
elif maritalStatus == "s" and earnedIncome >= 9951 and earnedIncome <= 40525 : #earned income between 9951 and 40525
	taxOwed = (9950 * .10) + ((earnedIncome - 9950) * .12) #takes 10% from 9950 and 12% from earned income - 9950
	print("You owe",taxOwed,"in taxes")
elif maritalStatus == "s" and earnedIncome >= 40526 and earnedIncome <= 86375 : #earned income between 40526 and 86375
	taxOwed = (9950 * .10) + ((40525 - 9950) * .12) + ((earnedIncome - 40525) * .22) #takes 10% from 9950, 12% from 40525 - 9950 and 22% from earned income - 40525
	print("You owe",taxOwed,"in taxes")
elif maritalStatus == "s" and earnedIncome > 86375 : #if the person earned more than 86375
	print("you make too much for this calculator!")

#If the person is married
if  maritalStatus == "m" and earnedIncome <= 19900 : #Martial status is married # first if for under 19900
	taxOwed = earnedIncome * .10
	print("You owe",taxOwed,"in taxes")
elif maritalStatus == "m" and earnedIncome >= 19901 and earnedIncome <= 81050 : #Earned income between 19901 and 81050
	taxOwed = (19900 * .10) + ((earnedIncome - 19900) * .12) #takes 10% from 19900 and 12% of earned income - 19900
	print("You owe",taxOwed,"in taxes")
elif maritalStatus == "m" and earnedIncome >= 81051 and earnedIncome <= 172750 : #earned income between 81051 and 172750
	taxOwed = (19900 * .10) + ((81050 - 19900) * .12) + ((earnedIncome - 81050) * .22) #takes 10% from 19900, 12% from 81050 - 19900, and 22% from earned income - 81050
	print("You owe",taxOwed,"in taxes")
elif maritalStatus == "m" and earnedIncome > 172751 : #Martial status is married and earned more than 172751
	print("you make too much for this calculator!")


# 