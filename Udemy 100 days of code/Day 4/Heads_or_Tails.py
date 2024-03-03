playing=True
while playing==True:
  import os
  os.system('cls' if os.name == 'nt' else 'clear')
  import random
  coin=random.randint(0,1)
  print("Welcome to the coin flipper!\n_____________________________")
  if coin==1:
    print("Flipping the coin...\n")
    input("Press enter to see the result")
    print("\n You flipped Heads!")
    flip_again=input("\nWould you like to flip again? (yes/no)").lower()
    if flip_again=="no":
      playing=False
      input("Press enter to exit")
  else:
    print("Flipping the coin...\n")
    input("Press enter to see the result")
    print("\n You flipped Tails!")
    flip_again=input("\nWould you like to flip again? (yes/no)").lower()
    if flip_again=="no":
      playing=False
      input("Press enter to exit")