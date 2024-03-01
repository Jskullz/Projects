#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill=float(input("How much was your bill today? "))
people= int(input("How many people would you like to split the bill between? "))
tip= int(input("What percentage of tip would you like to leave? "))

tip_percent= tip/100

tip_total=(bill/people*tip_percent)
total=tip_total+bill
final_total= round(total, 2)
print(f"Each person should be paying ${total:.2f}")