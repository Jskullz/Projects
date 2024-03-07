# #Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. 
# If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# # Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
import os
def lovefunc( flower1, flower2 ):
    if (flower1 % 2 == 0) and (flower2 % 2 == 1):
        return True
    elif (flower2 %2 == 0) and (flower1 %2 == 1):
        return True
    else:
        return False
def valid_input(number):
    if number.isdigit()==True:
        return True
    else:
        print("Invalid input. please enter a number.\n")
        return False
    
playing=True
while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the flower love calculator.")
    flower1=input("How many petals does the first flower have? ")
    while not valid_input(flower1):
        flower1=input("How many petals does the first flower have? ")

    flower2=input("How many petals does the second flower have? ")

    while not valid_input(flower2):
        flower2=input("How many petals does the second flower have? ")

    flower1=int(flower1)
    flower2=int(flower2)

    print(lovefunc(flower1,flower2))
    play_again=input("Do you want to check the flowers again? (yes/no) ")

    while play_again.lower() != "yes" and play_again.lower() != "no":
        print("Invalid Input.")

        play_again = input("Do you want to check the flowers again? (yes/no) ")
    if play_again.lower() == "no":
        playing = False
        print("Goodbye.")
        input("Press enter to exit.")
    


                          