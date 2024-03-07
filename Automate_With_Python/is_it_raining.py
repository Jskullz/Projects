def valid_input(answer):
    if answer.lower() == "yes" or answer.lower() == "no":
        return True
    else:
        return False

check_weather = True
while check_weather:
    raining_no_umbrella = False
    raining = input("Is it raining? (yes/no) ")
    while not valid_input(raining):
        print("Invalid input.")
        raining = input("Is it raining? (yes/no) ")
    if raining.lower() == "yes":
        umbrella = input("Do you have an umbrella? (yes/no) ")
        while not valid_input(umbrella):
            print("Invalid input.")
            umbrella = input("Do you have an umbrella? (yes/no) ")
        if umbrella.lower() == "yes":
            print("Go outside.")
        elif umbrella.lower() == "no":
            print("Wait a while.")
            raining_no_umbrella = True
            while raining_no_umbrella:
                raining = input("Is it still raining? (yes/no) ")
                while not valid_input(raining):
                    print("Invalid input.")
                    raining = input("Is it still raining? (yes/no) ")
                if raining.lower() == "yes":
                    print("Wait a while.")
                else:
                    print("Go outside.")
                    raining_no_umbrella = False
        else:
            print("Invalid input.")
    else:
        print("Go outside.")
    play_again = input("Do you want to check the weather again? (yes/no) ")
    while play_again.lower() != "yes" and play_again.lower() != "no":
        print("Invalid Input.")
        play_again = input("Do you want to check the weather again? (yes/no) ")
    if play_again.lower() == "no":
        check_weather = False
        print("Goodbye.")
        input("Press enter to exit.")
