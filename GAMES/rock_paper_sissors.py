playing=True
while playing:
    rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

    paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

    scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


    import random
    your_choice=input("Rock,Paper,Scissors What will you choose: ")
    if your_choice.lower()=="rock":
        print(f"You Picked: {rock}")
    elif your_choice.lower()=="paper":
        print(f"You Picked is: {paper}")
    else:
        print(f"You Picked is: {scissors}")

    choices=["rock","paper","scissors"]
    choices_length=len(choices)
    computers_choice=random.randint(0,choices_length)-1
    computers_choice_final=choices[computers_choice]

    if computers_choice_final=="rock":
        print(f"The Computer Picked {rock}")
    elif computers_choice_final=="paper":
        print(f"The Computer Picked {paper}")
    elif computers_choice_final=="scissors":
        print(f"The Computer Picked {scissors}")
    else:
        print("Invalid")

    #Rock beats scissors
    #paper beats rock
    #scissors beats paper
    if your_choice.lower()=="rock" and computers_choice_final=="scissors":
        print("Congratulations! You've smashed your way to victory! \nYou're now on your way to becoming a world champion!")
        play=input("Do you want to play again? (yes/no): ")
        if play.lower()=="no":
            playing=False
    elif your_choice.lower()=="paper" and computers_choice_final=="rock":
        print("Hooray! You've wrapped up victory! \nGet ready to roll as you climb the ladder to becoming a world champion!")
        play=input("Do you want to play again? (yes/no): ")
        if play.lower()=="no":
            playing=False
    elif your_choice.lower()=="scissors" and computers_choice_final=="paper":
        print("Snip, snip, hooray! \nYou've cut through the competition and emerged victorious! \nThe path to becoming a world champion lies ahead!")
        play=input("Do you want to play again? (yes/no): ")
        if play.lower()=="no":
            playing=False
    elif your_choice.lower()==computers_choice_final:
        print("It's a draw! A battle of equals.\n Keep pushing forward on your journey to becoming a world champion!")
        play=input("Do you want to play again? (yes/no): ")
        if play.lower()=="no":
            playing=False
    else:
        print("YOU LOSE! Don't give up! \nEvery defeat is a step closer to your ultimate victory as a world champion!")
        play=input("Do you want to play again? (yes/no): ")
        if play.lower()=="no":
            playing=False