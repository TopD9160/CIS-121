#create script asking user for their name and income. Let them know how much money they would have if they dont spend any money in 20 years

#ex hey "name", you make "income" a year!
# this is how much money you would have in 20 years

year = 0

name = input("what is your name? ")
income = int(input("What is your income? "))
total_income = 0

while year < 20 :
   if year <= 20 :
      year = year + 1
      total_income = total_income + income
      print(total_income,"year",year)
   elif year == 20 :
      print("Hey",name,"you make",income,"a year!")
      print("You will make",total_income,"in 20 years")
