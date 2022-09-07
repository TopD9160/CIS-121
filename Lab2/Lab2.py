# Combination of dog,cat,and horse years

#########
human_age = float(input("how old are you?"))
#########


dog_year = 7 # 1 human year is 7 dog
human_in_dog_years = dog_year * human_age

print("an human aged",human_age,"year old human would be",human_in_dog_years ,"years")


########
#Cat Years
cat_year = 9
human_in_cat_years = cat_year * human_age #cat year human age * 9

print("an human aged",human_age,"year old human would be",human_in_cat_years,"years")


########
#Horse Years
horse_years = 3 * ((((human_age**2 - 47)/7))+12)

print("an human aged",human_age,"year old human would be",horse_years,"years")