age = input("How old are you? ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
#Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
weeks_until_90 = 4680
age_int=int(age)

age_in_weeks = age_int*52

weeks_left = weeks_until_90 - age_in_weeks
weeks_left_round = round(weeks_left)

#It will take your current age as the input and output a message with our time left in this format:
print(f"You have {weeks_left_round} weeks left to live assuming you live until youre 90.")
#You have x weeks left.