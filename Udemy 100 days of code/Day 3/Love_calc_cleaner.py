playing = True
while playing == True:
  import os
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Welcome to the Love Calculator!\n______________________________\n")


  name1 = input("What is your name:")  # What is your name?
  name2 = input("What is your partners name:")  # What is their name?
  print("\nThe Love Calculator is calculating your score...")
  input("Press enter to see your score")
  # Your code below this line 👇
  combined_names = name1 + name2
  lower_names = combined_names.lower()
  t = lower_names.count("t")
  r = lower_names.count("r")
  u = lower_names.count("u")
  e = lower_names.count("e")
  first_digit = t + r + u + e

  l = lower_names.count("l")
  o = lower_names.count("o")
  v = lower_names.count("v")
  e = lower_names.count("e")
  second_digit = l + o + v + e

  score = int(str(first_digit) + str(second_digit))
  if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
  elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
  else:
    print(f"Your score is {score}.")
  flip_again = input("\nWould you like to check another couple? (yes/no)").lower()
  if flip_again == "no":
    playing = False
    input("Press enter to exit")
