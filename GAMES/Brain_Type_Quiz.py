print("""
 ____            _         _____                    ___        _     
| __ ) _ __ __ _(_)_ __   |_   _|   _ _ __   ___   / _ \ _   _(_)____
|  _ \| '__/ _` | | '_ \    | || | | | '_ \ / _ \ | | | | | | | |_  /
| |_) | | | (_| | | | | |   | || |_| | |_) |  __/ | |_| | |_| | |/ / 
|____/|_|  \__,_|_|_| |_|   |_| \__, | .__/ \___|  \__\_\\__,_|_/___|
                                |___/|_|                             
      """)
playing=True
braintype=""
def tora():
    print("Welcome to the Tora Brain Type!")
    tora_categories = {
    "1": "\nUnderstanding the Torah Brain Type:The Torah brain type is characterized by hard work, dedication, and intense ambition. \nHowever, this ambition can sometimes lead to burnout if not managed properly. \nUnderstanding the unique neurobiology of the Torah brain type can help individuals reach their full potential.\n",
    "2": "\nTraits and Characteristics:Torahs are fire types, meaning they exhibit intense traits and strong responses to their beliefs and goals. They are incredibly passionate and driven individuals who are \noften described as 'rookies with purpose.' The prefrontal circuits in their brains are wired for strong emotional responses, especially when pursuing their objectives.\nThey are confident, competitive, and resilient in the face of challenges. Torahs approach learning and problem-solving in a systematic and strategic manner.\nThey are purpose-driven and develop a curiosity about what they learn, using it as fuel to hunt for answers and achieve their goals. Torahs benefit from having clearly defined \nlearning objectives and goals, which make them unstoppable in their pursuit of knowledge.\n",
    "3": "\nMotivation, Productivity, and Self-Discovery:One of the most powerful qualities of Torahs is their limitless motivation. They have a fiery passion for what they do and rarely give up. \nHowever, this intense motivation can lead to burnout if not managed properly. Torahs should be mindful of taking breaks and scheduling time for recovery to maintain the quality of their work and\nproductivity levels. The Torah club emphasizes self-discovery and personal reflection. Torahs should not feel confined by their brain type but rather use it as a \nguide for personal growth and development. While Torahs are ambitious and often become great leaders, they should also recognize that other aspects of their \npersonality, such as Kuma or Kitsune energy, may come into play. Embracing all facets of their identity can lead to holistic personal and professional success.\n",
    }
    print("Here are some traits of the Tora brain type:")
    print("1. Understanding the Torah Brain Type")
    print("2. Traits and Characteristics")
    print("3. Motivation, Productivity, and Self-Discovery")

    
    learn = input("What would you like to learn more about? Enter a number: ")
    if learn in tora_categories:
        print(tora_categories[learn])
    else:
        print("Invalid trait selected.")


    

def kitsune():
    print("Welcome to the Kitsune Club!")
    kitsune_traits = {
        "1": "\nUnderstanding the Kitsune Brain Type: The Kitsune brain type is characterized by a love for learning, adaptability, and a tendency to be easily distracted. \nUnderstanding the unique neurobiology of the Kitsune brain type can help individuals leverage their strengths and overcome their \nchallenges to reach their full potential.",
        "2": "\nTraits and Learning Style:Kitsunes, wind types, are charismatic, creative, and live dramatically.\nTheir limbic system is highly reactive, making them curious, sensitive, and spontaneous.\nThey approach problem-solving by diving in headfirst, preferring to try first and think later. \nWhile they are fast learners, scheduling review time is essential for retention.\n ",
        "3": "\nCuriosity, Productivity, and Stress Management:The most powerful quality of Kitsunes is their boundless curiosity, but it can also lead to impulsivity and a lack of focus.\nThey thrive without strict schedules and prefer to follow their own interests throughout the day. However, they are highly \nsensitive and prone to stress, often exaggerating the consequences of situations. Mindfulness and bringing attention back to the present moment can help Kitsunes\nmanage stress and avoid getting lost in thought loops."
        
    }

    print("Here are some traits of the Kitsune Club:")
    print("1. Understanding the Kitsune Brain Type")
    print("2. Traits and Learning Style")
    print("3. Curiosity, Productivity, and Stress Management")
    

    learn = input("What would you like to learn more about? Enter a number: ")
    if learn in kitsune_traits:
        print(kitsune_traits[learn])
    else:
        print("Invalid trait selected.")


def kuma():
    print("Welcome to the Kuma Club!")
    kuma_traits = {
        "1": "\nUnderstanding the Kuma Brain Type: The Kuma brain type is characterized by discipline, consistency, and resilience. \nUnderstanding the unique neurobiology of the Kuma brain type can help individuals \nleverage their strengths and overcome challenges to reach their full potential.",
        "2": "\nTraits and Learning Style:Kumas, water types, are known for their calmness, patience, and methodical \napproach to problem-solving. They are thoughtful thinkers who carefully consider multiple perspectives and immerse themselves in their studies. \nWhile they may learn slowly, they retain information for longer periods. Gathering information from various sources\n is essential for Kumas to gain a well-rounded perspective and build momentum in their studies.\n",
        "3": "\nResilience, Productivity, and Stress Management:The most powerful quality of Kumas is their unwavering resilience.\nThey have exceptional endurance, both mentally and physically, and are less sensitive to external stimulation.\nWhile slow and steady wins the long game, Kumas may require additional motivation to get started and may take longer to make decisions. \nConsistency is key for Kumas, who thrive with rituals, habits, and routines. Stress for Kumas often stems from internal pressure to keep up with peers,\nleading to self-criticism and feelings of discouragement. Mindfulness, gratitude, and enjoying the journey\nrather than fixating on the destination can help Kumas manage stress and stay focused on their goals.\n",
    }

    print("Here are some traits of the Kuma Club:")

    learn = input("What would you like to learn more about? Enter a number: ")
    if learn in kuma_traits:
        print(kuma_traits[learn])
    else:
        print("Invalid trait selected.")


def test():
    def get_valid_input(prompt):
        while True:
            user_input = input(prompt).upper()
            if user_input in ['A', 'B', 'C']:
                return user_input
            else:
                print("\n")
                print("Invalid input! Please enter A, B, or C.")
                input("Press enter to continue\n")
                print("\n")
    print("Welcome to the Brain Type Quiz!\n")
    print("This quiz will help you determine your brain type!")
    print("Answer the questions with the following options: A, B, or C\n")
    print("Let's get started!")
    input("Press enter to continue\n")
    question_answers =[]
    print("The first question will determine how you approach learning.\n")
    question_1=get_valid_input("When playing a brand new game, how do you learn the instructions?\n A) I read the rules to determine the objectives. \n B) I hop in and start playing, and I learn as I go. \n C) I look for tutorials or guidance from someone else who has played the game.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_1)
    print("The Next question will test your decision making.")
    question_2=get_valid_input("When making important decisions, which type are you?\n A) I thoroulghly research all options before deciding. \n B) I go with my gut and pick what I intuitively like. \n C) I ask people I trust for recommendations.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_2)
    print("The next question is about your daily routine.")
    print("How do you prefer your daily routines to be?")
    question_3= get_valid_input(" A) I like to be goal-oriented for maximum productivity. \n B) I like to be flexible and adaptable to life. \n C) I like predictability and steady for consistency.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_3)
    print("The next question will test your energy")
    print("In general, how is your stamina over the course of a day?")
    question_4= get_valid_input(" A) Average, But I can push myself when needed. \n B) Mild, I tend to start strong with lots of energy, but lise steam. \n C) Enduring, I have great stamina, but don't typically reach my limit.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_4)
    print("The next question us about teamwork.")
    print("You are assigned to work on a group project. What role would you normally take?")
    question_5= get_valid_input(" A) I take the lead and delegate tasks. \n B) I excel in roles that require high technical skill. \n C) I perfer to help where needed and empower my team members.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_5)
    print("The next question is about planning.")
    print("How do you approach planning a vacation?")
    question_6= get_valid_input("A) I prepare an itinerary and schedule to follow. \nB) I want something flexible and spontaneous. \nC) I stick to what I know and enjoy familiarity.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_6)
    print("The next question will test your sleep")
    print("Describe your typical night of sleep.")
    question_7= get_valid_input("A) Moderate,regular sleeper. \nB) Light sleeper, I wake up easily. \nC)Deep sleeper, waking up in the morning is hard.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_7)
    print("The next question will test your appitite.")
    print("Describe your appetite on a typical day.")
    question_8= get_valid_input("A) I dont like to skip meals. I can get irritible when I miss them. \nB) It fluctuates. Sometimes I snack a lot, sometimes I forget to eat. \nC) I tend to feel full for a while after a meal. I can comfortable delay eating if needed.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_8)
    print("The next question will test your temperment.")
    print("In general, which of the following best describes you")
    question_9= get_valid_input("A) Purposeful and goal-oriented. \nB) Enthusiastic and enjoy trying new things. \nC) Easygoing and go with the flow.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_9)
    print("The final question will test your response to stress.")
    print("You have an online assignment worth 50% of your grade.It is due in 15 minutes.\nBut the power and internet go out! During stress,what is usually the first\nemotion you feel?")
    question_10= get_valid_input("A) Frustration or irritability. \nB) Worry or Anxiety.\nC) Hopeless or loss of motivation.\nPlease enter your answer: ").upper()
    print("\n")
    question_answers.append(question_10)
    print("\n")
    print("Thank you for taking the quiz! Your results are being calculated.\n")
    input("Press enter to continue\n")
    tora=0
    kitsune=0
    kuma=0
    for answer in question_answers:
        if answer=="A":
            tora+=1
        elif answer=="B":
            kitsune+=1
        elif answer=="C":
            kuma+=1
    if tora>kitsune and tora>kuma:
        print("Your brain type is Tora!")
        print("Each brain type has its own unique strengths and weaknesses and you can have traits of other brain types as well.\nSo check out your score in each catagory to see which brain type you are most like!")
        print("Your scores in each category are as follows:" + "\n" + "Tora: " + str(tora) + "\n" + "Kitsune: " + str(kitsune) + "\n" + "Kuma: " + str(kuma) + "\n")
        print("Check out the info section to learn more about the Tora brain type!")
        input("Press enter to continue")
        
        
        
        
    elif kitsune>tora and kitsune>kuma:
        print("Your brain type is Kitsune!")
        print("Each brain type has its own unique strengths and weaknesses and you can have traits of other brain types as well.\n So check out your score in each catagory to see which brain type you are most like!")
        print("Your scores in each category are as follows:" + "\n" + "Tora: " + str(tora) + "\n" + "Kitsune: " + str(kitsune) + "\n" + "Kuma: " + str(kuma) + "\n")
        print("Check out the info section to learn more about the Kitsune brain type!")
        input("Press enter to continue")
        
        
        
    elif kuma>tora and kuma>kitsune:
        print("Your brain type is Kuma!")
        print("Each brain type has its own unique strengths and weaknesses and you can have traits of other brain types as well.\nSo check out your score in each catagory to see which brain type you are most like!")
        print("Your scores in each category are as follows:" + "\n" + "Tora: " + str(tora) + "\n" + "Kitsune: " + str(kitsune) + "\n" + "Kuma: " + str(kuma) + "\n")
        print("Check out the info section to learn more about the Kuma brain type!")
        input("Press enter to continue")
        
    else:
        print("You have a tie in your scores! You may have traits of multiple brain types.")
        print("Check out your score in each catagory to see which brain type you are most like!")
        print("Your scores in each category are as follows:" + "\n" + "Tora: " + str(tora) + "\n" + "Kitsune: " + str(kitsune) + "\n" + "Kuma: " + str(kuma) + "\n")
        print("Check out the info section to learn more about the Tora, Kitsune, and Kuma brain types!")
        input("Press enter to continue")

        
        
        
        
def brain_type_info():
    print("""
      _____ _   _ ______ ____    _____        _____ ______
     |_   _| \ | |  ____/ __ \  |  __ \ /\   / ____|  ____|
       | | |  \| | |__ | |  | | | |__) /  \ | |  __| |__  
       | | | . ` |  __|| |  | | |  ___/ /\ \| | |_ |  __|  
      _| |_| |\  | |   | |__| | | |  / ____ \ |__| | |____
     |_____|_| \_|_|    \____/  |_| /_/    \_\_____|______|
     __________________________________________________________                                                      """)
    print("""
     __________  ___  ___
    /_  __/ __ \/ _ \/ _ |
     / / / /_/ / , _/ __ |
    /_/  \____/_/|_/_/ |_|""")
    print("""
       __ __________________  ___  ______
      / //_/  _/_  __/ __/ / / / |/ / __/
     / ,< _/ /  / / _\ \/ /_/ /    / _/  
    /_/|_/___/ /_/ /___/\____/_/|_/___/""")
    print("""
        __ ____  ____  ______
      / //_/ / / /  |/  / _ |
     / ,< / /_/ / /|_/ / __ |
    /_/|_|\____/_/  /_/_/ |_|
          """)

    braintype=input("Which brain type would you like to learn more about?: ").lower()
    if braintype=="tora":
        tora_info=True
        while tora_info:
            tora()
            print("\n")
            tora_continue=input("Would you like to learn more about the Tora brain type? (yes/no): ").lower()
            if tora_continue=="no":
                tora_info=False
            elif tora_continue=="yes":
                tora_info=True
            else:
                print("Invalid input!")
                input("Press enter to continue")

    elif braintype=="kitsune":
        kitsune_info=True
        while kitsune_info:
            kitsune()
            print("\n")
            kitsune_continue=input("Would you like to learn more about the Kitsune brain type? (yes/no): ").lower()
            if kitsune_continue=="no":
                kitsune_info=False
            elif kitsune_continue=="yes":
                kitsune_info=True
            else:
                print("Invalid input!")
                input("Press enter to continue")
    elif braintype=="kuma":
        kuma_info=True
        while kuma_info:
            kuma()
            print("\n")
            kuma_continue=input("Would you like to learn more about the Kuma brain type? (yes/no): ").lower()
            if kuma_continue=="no":
                kuma_info=False
            elif kuma_continue=="yes":
                kuma_info=True
            else:
                print("Invalid input!")
                input("Press enter to continue")
    else:
        print("Invalid please choose Tora, Kitsune, or Kuma")    

while playing:
    choice=input("Would you like to take the brain type quiz or learn more about your brain type? (quiz/info/exit): ").lower()
    print("\n")
    if choice=="quiz":
        test()
    elif choice=="info":
        brain_type_info()
    elif choice=="exit":
        print("Goodbye")
        input("Press enter to exit")
        playing=False
    else:
        print("Invalid please choose quiz or info")
        
        
    