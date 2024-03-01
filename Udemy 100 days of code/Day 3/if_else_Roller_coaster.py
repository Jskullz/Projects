print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height>= 120:
    print("You are tall enough to ride! ")
    age=int(input("What is your age? "))
    if age <= 12:
        price=5
        print("Child ticket price is $5")
    elif age <=18:
        price=7
        print("Youth ticket price is $7")
    elif age>=70:
        price=5
        print("Senior discount ticket price is 5$")
    elif age >45 and age < 55:
        price=0
        print("Ticket prices are free")
    else:
        price=12
        print("Adult ticket price is $12")
    photo= input("do you want to buy a photo yes or no? ")
    if photo.lower() == "yes":
        price+= 3
        print(f"Your total will be ${price}")
    else:
        print(f"Your total will be ${price} thank you!")
        
else:
    print("Sorry, you are not tall enough to ride. ")