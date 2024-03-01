#Variables

ascii_art=(''' WELCOME TO TREASURE ISLAND
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
explore_cave=("""As you continue to explore the island, you stumble upon a mysterious 
cave entrance partially hidden by dense foliage. The darkness within seems ominous, 
but a glimmer of curiosity beckons you to investigate further.

What would you like to do next?

Enter the cave to explore its depths, intrigued by the possibility of hidden treasures.
Decide to play it safe and avoid the cave, continuing your exploration elsewhere on the island.
        
[Enter]     [Avoid]                           

              """)
start_game=("""You awaken to the sound of crashing waves, the taste of salt on your lips,
and the sensation of warm sand beneath you. As your eyes adjust to the sunlight, 
you realize you've washed ashore on a mysterious island known as Treasure Island. 
Memories of a shipwreck flood back to you, and you find yourself stranded 
with no sign of your crew or rescue in sight.

What would you like to do?

Explore the beach for any signs of your crew or supplies.
Search the nearby jungle for shelter and resources.
Take a moment to gather your bearings and assess the situation.
      
[Explore]     [Search]     [Rest]
      """)
found_map=("""
          
You decide to explore the island, hoping to find clues that might
lead to your rescue or at least provide some insight into your current predicament. 
As you walk along the shoreline, you spot a few scattered items washed up from the wreck. 
Among the debris, you notice a torn piece of parchment sticking out from the sand.

What would you like to do next?

Examine the parchment to see if it holds any valuable information.
Continue exploring the beach in search of other items or signs of your crew.
          
[Examine]     [Explore]""")
examine_map=("""You pick up the torn piece of parchment and carefully unfold it. 
It appears to be a fragment of an old map, with faded ink marking various landmarks 
on the island. Despite its age, the map seems to indicate a location deeper within
the jungle, marked with an "X" symbol.

What would you like to do next?

Follow the map's directions and head deeper into the jungle in search of the treasure.
Decide to hold onto the map for now and continue exploring the island for other clues or resources.
            
[Follow]     [Explore]         
              """)
search_island=("""Feeling a sense of urgency, you decide to venture into the dense jungle, hoping to find shelter, 
supplies, or any sign of your missing crew. The foliage looms overhead, casting intricate patterns of light 
and shadow on the forest floor as you push forward.
After a few minutes of trekking through the undergrowth, you stumble upon a clearing. 
To your left, you notice the remnants of what appears to be a makeshift shelter, constructed from branches and leaves.
To your right, a small stream trickles through the foliage, offering a potential source of fresh water.

What would you like to do next?

Investigate the makeshift shelter to see if there are any usable supplies or clues left behind.
Follow the stream deeper into the jungle in search of more resources or signs of civilization.
          
[Left]     [Right]  """)
rest= ("""Feeling overwhelmed by the situation, you decide to take a moment to rest and collect your thoughts.
You sink back into the warm sand, allowing the gentle rhythm of the waves to soothe your frazzled nerves. 
Closing your eyes, you focus on slowing your breathing and calming your mind.
After a few moments of relaxation, you feel a sense of rejuvenation coursing through your body. 
However, the reality of your predicament still looms over you, urging you to take action.

What would you like to do next?

Continue resting until help arrives.
Rise to your feet and explore the beach in search of any signs of your crew or supplies.
[Rest]     [explore] """)
cave_or_map=("""You're intrigued by the possibilities presented by the old map and decide to follow its directions deeper 
into the dense jungle. The canopy overhead casts dappled shadows on the forest floor as you push through the tangled undergrowth, 
following the faded landmarks marked on the parchment.

After what feels like hours of navigating through the dense vegetation, you come across a narrow opening hidden amidst the thick foliage.
The entrance to a dark and mysterious cave lies before you, beckoning with the promise of untold secrets and hidden treasures.

What would you like to do next?

Summon your courage and venture into the depths of the cave, determined to uncover the treasure marked on the map.
Decide to continue following the map's directions deeper into the woods, hoping to find the treasure without entering the cave just yet.
                  
[Cave]     [Woods]""")
cave_bad_ending=("""You summon your courage and venture into the depths of the cave, determined to uncover the treasure marked on the map. 
As you step into the darkness, the cool, damp air envelops you, and the sound of your footsteps echoes off the rocky walls.
However, as you proceed deeper into the cave, the passage narrows and twists, making it increasingly difficult to find your way. 
The dim light filtering in from the entrance fades, leaving you stumbling blindly in the darkness.
Suddenly, you feel the ground give way beneath you, and you plummet into a hidden pit, landing with a bone-jarring thud. 
You struggle to your feet, but it's too late—you're trapped in the depths of the cave with no hope of escape.
As panic sets in, you realize that your quest for treasure has led you to a perilous end. Alone and lost in the darkness,
you can only wonder what other dangers lie hidden within the depths of Treasure Island's caves.

[End - Bad Ending]""")
walk_from_cave_good_ending=("""You stand before the dark entrance of the cave, feeling a sense of unease creep over you. Rather than risking the unknown dangers within,
you decide to proceed with caution and continue following the map's directions deeper into the jungle.
As you backtrack from the cave entrance and resume your journey through the dense vegetation, you remain vigilant, keeping a keen eye on the landmarks indicated on the old map. 
The forest grows thicker, and the air becomes heavy with the scent of damp earth and tropical flora.
After what feels like an eternity of winding through the labyrinthine paths of the jungle, you finally come upon a clearing. 
In the center of the clearing stands a weathered stone pedestal, atop which rests a gleaming chest adorned with intricate carvings.
With a rush of excitement, you realize that you've stumbled upon the treasure marked on the map—a tangible reward for your perseverance and caution. 
You approach the chest and carefully lift the lid, revealing a dazzling array of jewels and ancient artifacts within.
As you marvel at your discovery, a sense of relief and accomplishment washes over you. Despite the challenges and dangers you've faced, you've emerged victorious,
with treasure in hand and a thrilling tale to tell.

[End - Good Ending]""")

Waiting_for_rescue_bad_ending=(""" You decide to wait for rescue, hoping that help will arrive soon. You find a relatively safe spot near the stream and settle in,
scanning the horizon for any signs of approaching ships or aircraft.Hours turn into days, and days turn into weeks, but no rescue comes. The sun beats down relentlessly, 
and your provisions begin to dwindle. Despite your best efforts to ration food and water, your supplies eventually run out, leaving you weak and desperate.
As the days stretch on with no sign of rescue, despair sets in. You realize that you've pinned all your hopes on a rescue that may never come. In the end, your decision to wait
proves fatal as you succumb to hunger, thirst, and exhaustion.
Alone and forgotten on Treasure Island, your story becomes just another tragic tale lost to the depths of history.

[End - Bad Ending] """)
Rest_River=("""Feeling rejuvenated by the tranquil atmosphere of the waterfall, you take a moment to gather your thoughts and assess your surroundings. As you sit beside the crystal-clear pool,
                 
you notice various objects scattered along the streambank—rocks, branches, and vines. With a spark of ingenuity, you begin to experiment with the materials, fashioning them into a makeshift weapon. 
Despite its simplicity, you're satisfied with the result—a crude but serviceable tool that may prove invaluable in the wilderness.
Armed with your newly crafted weapon, you feel a surge of confidence coursing through you. The jungle may be teeming with unknown dangers, but you're ready to face them head-on.

What's your next move?

Will you continue your journey deeper into the jungle, armed and ready for whatever challenges lie ahead? Or will you wait for rescue, hoping that help will arrive soon?

[Explore] [Wait for Rescue] 
                  """)
found_monkey=("""As you venture deeper into the dense jungle, the foliage thickens, and the air becomes heavy with the scent of exotic flowers and damp earth. 
                   
Suddenly, movement catches your eye—a small figure swinging through the trees with agile grace.You pause, captivated by the sight of a mischievous monkey frolicking among the branches.
Its curious eyes meet yours, and for a moment, you share a silent exchange, each sizing up the other.

What will you do next?

Approach the monkey cautiously, hoping to establish a friendly rapport and perhaps gain a helpful companion in your journey.
Decide to keep your distance and quietly retreat, wary of the unpredictable nature of wild animals and the potential risks they pose.

[Approach] [Run Away]""")
cave_good_end=("""Summoning your courage, you decide to venture into the depths of the cave, intrigued by the possibility of uncovering hidden treasures. As you step into the darkness, the cool, 
damp air envelops you, and the sound of your footsteps echoes off the rocky walls.Equipped with your makeshift weapon and the glow of a torch fashioned from materials 
found near the stream, you cautiously advance deeper into the cavern. The dim light flickers and dances across the ancient walls, casting eerie shadows that seem to come alive in the darkness.
Despite the trepidation gnawing at your gut, you press on, driven by a sense of curiosity and adventure. As you navigate the winding passages, your torch illuminates the way,
revealing tantalizing glimpses of glittering gemstones and ancient artifacts embedded in the walls. Finally, after what feels like an eternity of exploration, you stumble upon a 
chamber bathed in soft light, its floor strewn with treasures beyond your wildest dreams. Jewels sparkle in the faint glow, and precious artifacts whisper tales of a bygone era.
Overwhelmed with awe and wonder, you realize that you've stumbled upon the fabled treasure of Treasure Island—the culmination of your perilous journey. With a sense of triumph and satisfaction,
you gather the riches and prepare to make your way back to civilization, eager to share your incredible tale with the world.

[End - Good Ending]""")

Monkey_cave=("""Summoning your courage, you decide to venture into the depths of the cave, intrigued by the possibility of uncovering hidden treasures.
 As you step into the darkness, the cool, damp air envelops you, and the sound of your footsteps echoes off the rocky walls.
With your loyal monkey companion by your side, you rely on its knowledge of the island to navigate the winding passages. The monkey deftly leads the way,
guiding you through the labyrinthine tunnels with ease.Despite the trepidation gnawing at your gut, you press on, driven by a sense of curiosity and adventure. 
As you explore further, the dim light flickers and dances across the ancient walls, revealing tantalizing glimpses of glittering gemstones and ancient artifacts embedded in the walls.
Finally, after what feels like an eternity of exploration, you stumble upon a chamber bathed in soft light, its floor strewn with treasures beyond your wildest dreams.
Jewels sparkle in the faint glow, and precious artifacts whisper tales of a bygone era.
Overwhelmed with awe and wonder, you and your faithful monkey companion realize that you've stumbled upon the fabled treasure of Treasure Island—the culmination of your perilous journey.
With a sense of triumph and satisfaction, you gather the riches and prepare to make your way back to civilization, eager to share your incredible tale with the world.

[End - Good Ending]""")
Cave_No_Monkey=("""As you continue to explore the island, your heart still racing from the encounter with the monkey, you stumble upon a 
mysterious cave entrance partially hidden by dense foliage.The darkness within seems ominous, but a glimmer of curiosity beckons you to investigate further.

What would you like to do next?

Enter the cave to explore its depths, intrigued by the possibility of hidden treasures.
Decide to play it safe and avoid the cave, continuing your exploration elsewhere on the island.

[Enter] [Avoid]""")
Right_River=("""You decide to follow the stream, hoping it will lead you to more resources or perhaps even signs of civilization. 
The water trickles gently over smooth stones, offering a soothing soundtrack to your journey through the dense jungle.
As you venture deeper into the undergrowth, the foliage grows thicker, and the sounds of wildlife become more pronounced. 
You catch glimpses of colorful birds flitting among the trees and hear the distant chatter of monkeys swinging through the canopy above.
After some time, you come upon a small waterfall cascading into a crystal-clear pool. The air is cool and refreshing, and you can't help but feel a sense of tranquility wash over you.

What would you like to do next?

Take a moment to rest and replenish your energy by the waterfall.
Continue following the stream deeper into the jungle, determined to uncover whatever secrets it may hold.

[Rest] [Continue]

""")

Go_back_to_cave_armed=("""Feeling rejuvenated by the tranquil atmosphere of the waterfall, you take a moment to gather your thoughts and assess your surroundings. As you sit beside the crystal-clear pool,
you notice various objects scattered along the streambank—rocks, branches, and vines. With a spark of ingenuity, you begin to experiment with the materials, fashioning them
into a makeshift weapon. Despite its simplicity, you're satisfied with the result—a crude but serviceable tool that may prove invaluable in the wilderness.
Armed with your newly crafted weapon, you feel a surge of confidence coursing through you. The jungle may be teeming with unknown dangers, but you're ready to face them head-on.

What's your next move?

Will you go back to the cave with your new supplies, eager to uncover its secrets armed and ready? Or will you wait for rescue, hoping that help will arrive soon?

[Enter Cave] [Wait for Rescue]""")
