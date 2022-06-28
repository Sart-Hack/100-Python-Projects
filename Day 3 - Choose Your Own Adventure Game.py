# This is day 3 project for the 100 Days of Python Course


char_name = input("Enter your character name: \n")
print(f"Welcome to Treasure Island {char_name}. Your mission is to find the treasure.")

choice_1 = input(f"Time to make your first choice {char_name}.\nDo you want to go left or right?\n")
if choice_1.lower() == "left":
    choice_2 = input(f"{char_name}, you see a lake in front of you. Do you swim or wait for a boat.\n")
    if choice_2.lower() in ("wait", "wait for boat"):
        choice_3 = input(f"{char_name}, you see 3 doors in front of you: Red, Blue and Yellow. Which one do you enter?\n")
        if choice_3.lower() in ("red","red door"):
            print(f"{char_name}, You were engulfed in scorching flames of fire and obviously died. Game over.")
        elif choice_3.lower() in ("blue", "blue door"):
            print(f"{char_name}, You find yourself in a room filled with ravaging and hungry beasts. \n"
                  f" They all attack you at once, eating you alive. Game Over")
        elif choice_3.lower in ("yellow", "yellow door"):
            print(f"Congratulations {char_name}! You found the treasure. You win!")
            print('''
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
        else:
            print("Invalid door. Game Over.")
    else:
        print(f"{char_name}, you were attacked by a trout in the middle of the lake and died a horrible death. Game over.")

else:
    print(f"{char_name}, you fall into a hole. Game over ")

