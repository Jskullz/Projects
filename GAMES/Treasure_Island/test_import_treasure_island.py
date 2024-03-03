import treasure_story_line
print(treasure_story_line.art)
print(treasure_story_line.start_game)
choice_1=input("What will you do?:  ")


if choice_1.lower() == "explore":
    print(treasure_story_line.found_map)
    #[Examine]     [Explore]
    choice_2=input("What will you do: ")
    if choice_2.lower()== "examine":
        print(treasure_story_line.examine_map)    
# [Follow]     [Explore]         
   
        choice_3=input("What will you do: ")  
        if choice_3.lower() == "follow":
            print(treasure_story_line.follow_map_found_cave)
            choice_4=input("What will you do: ")
            if choice_4.lower() == "enter":
                print(treasure_story_line.cave_bad_ending_no_supplies)
                input("Press Enter to exit...")
            else:
                print(treasure_story_line.follow_map_instead_of_cave_good_ending)
                input("Press Enter to exit...")
        else:
            print(treasure_story_line.found_cave_no_map)
            choice_4=input("What will you do: ")
            if choice_4.lower()=="enter":
                print(treasure_story_line.cave_bad_ending_no_supplies)
                input("Press Enter to exit...")
            else:
                print(treasure_story_line.examine_map_after_cave)
                choice_5=input("What will you do: ")
                if choice_5.lower()=="follow":
                    print(treasure_story_line.follow_map_good_ending)
                    input("Press Enter to exit...")
                else:
                    print(treasure_story_line.ate_by_wolves_bad_ending)  
                    input("Press Enter to exit...")      
    else:
        print(treasure_story_line.monkey_encounter)
        choice_3=input("What will you do: ")
        if choice_3.lower()== "approach":
            print(treasure_story_line.monkey_companion)
            choice_4=input("What will you do: ")
            if choice_4.lower() =="run":
                print(treasure_story_line.runaway_with_monkey)
                choice_5=input("What will you do: ")
                if choice_5.lower()=="enter":
                    print(treasure_story_line.cave_with_monkey_good_ending)
                else:
                    print(treasure_story_line.wait_for_rescue_bad_ending_with_monkey)
                    input("Press Enter to exit...")

            else:
                print(treasure_story_line.Investigate_tiger_bad_ending)
                input("Press Enter to exit...")
        else:
            print(treasure_story_line.run_from_monkey_find_cave)
            choice_4=input("What will you do: ")
            if choice_4.lower() == "enter":
                print(treasure_story_line.cave_bad_ending_no_supplies)
                input("Press Enter to exit...")
            else:
                print(treasure_story_line.run_from_cave_explore)
                choice_5=input("What will you do: ")
                if choice_5.lower() == "right":
                    print(treasure_story_line.right_find_stream)
                    choice_6=input("What will you do: ")
                    if choice_6.lower() == "rest":
                        print(treasure_story_line.rest_by_stream)
                        choice_7=input("What will you do: ")
                        if choice_7.lower() == "cave":
                            print(treasure_story_line.cave_with_supplies_good_ending)
                            input("Press Enter to exit...")
                        else:
                            print(treasure_story_line.wait_for_rescue_bad_ending)
                            input("Press Enter to exit...")
                    else:
                        print(treasure_story_line.found_cave_no_map)
                        choice_8=input("What will you do: ")
                        if choice_8.lower() == "enter":
                            print(treasure_story_line.cave_bad_ending_no_supplies)
                            input("Press Enter to exit...")
                        else:
                            print(treasure_story_line.found_map)
                            choice_9=input("What will you do: ")
                            if choice_9.lower() == "examine":
                                print(treasure_story_line.examine_map)    
                                choice_10=input("What will you do: ")  
                                if choice_10.lower() == "follow":
                                    print(treasure_story_line.follow_map_found_cave)
                                    choice_11=input("What will you do: ")
                                    if choice_11.lower() == "enter":
                                        print(treasure_story_line.cave_bad_ending_no_supplies)
                                        input("Press Enter to exit...")
                                    else:
                                        print(treasure_story_line.follow_map_instead_of_cave_good_ending)
                                        input("Press Enter to exit...")
                                else:
                                    print(treasure_story_line.found_cave_no_map)
                                    choice_12=input("What will you do: ")
                                    if choice_12.lower()=="enter":
                                        print(treasure_story_line.cave_bad_ending_no_supplies)
                                        input("Press Enter to exit...")
                                    else:
                                        print(treasure_story_line.examine_map_after_cave)
                                        choice_13=input("What will you do: ")
                                        if choice_13.lower()=="follow":
                                            print(treasure_story_line.follow_map_good_ending)
                                            input("Press Enter to exit...")
                                        else:
                                            print(treasure_story_line.ate_by_wolves_bad_ending)
                                            input("Press Enter to exit...")
                        
                else:
                    print(treasure_story_line.shelter)
                    choice_6=input("What will you do: ")
                    if choice_6.lower() == "explore":
                        print(treasure_story_line.found_cave_no_map)
                        choice_7=input("What will you do: ")
                        if choice_7.lower()=="enter":
                            print(treasure_story_line.cave_with_supplies_good_ending)
                            input("Press Enter to exit...")
                        else:
                            print(treasure_story_line.wait_for_rescue_bad_ending)
                            input("Press Enter to exit...")
                    else:
                        print(treasure_story_line.wait_for_rescue_bad_ending)
                        input("Press Enter to exit...")


elif choice_1.lower() == "search":
    print(treasure_story_line.stream_or_shelter)
    choice_2=input("What will you do?:  ")
    if choice_2.lower() == "right":
        print(treasure_story_line.right_find_stream)
        choice_3=input("What will you do?:  ")
        if choice_3.lower()=="rest":
            print(treasure_story_line.rest_by_stream)
            choice_4=input("What will you do?:  ")
            if choice_4.lower()=="explore":
                print(treasure_story_line.found_cave_no_map)
                choice_5=input("What will you do?:  ")
                if choice_5.lower()=="enter":
                    print(treasure_story_line.cave_with_supplies_good_ending)
                    input("Press Enter to exit...")
                else:
                    print(treasure_story_line.wait_for_rescue_bad_ending)
                    input("Press Enter to exit...")
            else:
                print(treasure_story_line.wait_for_rescue_bad_ending)
                input("Press Enter to exit...")
        else:
            print(treasure_story_line.found_cave_no_map)
            choice_4=input("What will you do?:  ")
            if choice_4.lower()=="enter":
                print(treasure_story_line.cave_bad_ending_no_supplies)
            else:
                print(treasure_story_line.found_map)
                choice_5=input("What will you do?:  ")
                if choice_5.lower()=="examine":
                    print(treasure_story_line.examine_map)
                    choice_6=input("What will you do?:  ")
                    if choice_6.lower()=="follow":
                        print(treasure_story_line.follow_map_found_cave_again)
                        choice_7=input("What will you do?:  ")
                        if choice_7.lower()=="enter":
                            print(treasure_story_line.cave_bad_ending_no_supplies)
                        else:
                            print(treasure_story_line.follow_map_instead_of_cave_good_ending)
                            input("Press Enter to exit...")
                    else:
                        print(treasure_story_line.ate_by_wolves_bad_ending)
                        input("Press Enter to exit...")
                else:
                    print(treasure_story_line.monkey_encounter)
                    choice_6=input("What will you do?:  ")
                    if choice_6.lower()=="approach":
                        print(treasure_story_line.monkey_companion)
                        choice_7=input("What will you do?:  ")
                        if choice_7.lower()=="run":
                            print(treasure_story_line.runaway_with_monkey)
                            choice_8=input("What will you do?:  ")
                            if choice_8.lower()=="enter":
                                print(treasure_story_line.cave_with_monkey_good_ending)
                                input("Press Enter to exit...")
                            else:
                                print(treasure_story_line.wait_for_rescue_bad_ending_with_monkey)
                                input("Press Enter to exit...")
                        else:
                            print(treasure_story_line.Investigate_tiger_bad_ending)
                            input("Press Enter to exit...")
                    else:
                        print(treasure_story_line.ate_by_wolves_bad_ending)
                        input("Press Enter to exit...")
    
    elif choice_2.lower()=="left":
        print(treasure_story_line.shelter)
        choice_3=input("What will you do?:  ")
        if choice_3.lower()=="explore":
            print(treasure_story_line.found_cave_no_map)
            choice_4=input("What will you do?:  ")
            if choice_4.lower()=="enter":
                print(treasure_story_line.cave_with_supplies_good_ending)
                input("Press Enter to exit...")
            else:
                print(treasure_story_line.wait_for_rescue_bad_ending)
                input("Press Enter to exit...")
        else:
            print(treasure_story_line.wait_for_rescue_bad_ending)
            input("Press Enter to exit...")
    else:
        print("invalid input, please try again.")
        input("Press Enter to exit...")


else:
    print("invalid input, please try again.")
    input("Press Enter to exit...")