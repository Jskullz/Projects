# Which year do you want to check?
year = int(input("Type a year you would like to check for a leap year. "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
#If cleanly divisible by 4 go to Is divisible by 100
if year%4==0:
#If not divisible go to not leap year
  if year%100==0:
    #if not divisible by 100 go to is leap year, else is divisible by 400
    if year%400==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")