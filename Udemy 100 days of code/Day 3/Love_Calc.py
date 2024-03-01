print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is your partners name?") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
score_true=0
score_love=0
#count true letters in each name
letter_count= name1.lower().count("t")+name1.lower().count("r")+name1.lower().count("u")+name1.lower().count("e")
score_true+=letter_count
letter_count_2= name2.lower().count("t")+name2.lower().count("r")+name2.lower().count("u")+name2.lower().count("e")
score_true+=letter_count_2

#count love letters in name
count_love_1=name1.lower().count("l")+name1.lower().count("o")+name1.lower().count("v")+name1.lower().count("e")
count_love_2=name2.lower().count("l")+name2.lower().count("o")+name2.lower().count("v")+name2.lower().count("e")
score_love+=count_love_1
score_love+=count_love_2

#add the 2 scores by first number
score_true=str(score_true)
score_love=str(score_love)
true_love_score=int(score_true+score_love)

#create if statements
if true_love_score <10 or true_love_score >90:
  print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif true_love_score >40 and true_love_score <50:
  print(f"Your score is {true_love_score}, you are alright together.")
else:
  print(f"Your score is {true_love_score}.")
