#Create a function which answers the question "Are you playing banjo?".#
#If your name starts with the letter "R" or lower case "r", you are playing banjo!#
def are_you_playing_banjo():
    name=input("What is your name?")
    if name.lower().startswith("r"):
        print("You are playing banjo!")
    else:
        print("You are not playing banjo!")
are_you_playing_banjo()
