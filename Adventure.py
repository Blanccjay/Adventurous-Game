# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 02:10:37 2024

@author: thant
"""

import sys

# Welcome the player
name = input("Type your name: ")
print("Welcome", name, ", to this crazy adventure!")

# Start of the adventure
print("You find yourself at the edge of an ancient, enchanted forest. Legends say it is filled with magical creatures, hidden treasures, and untold dangers. As you step into the forest, you must choose your path wisely.")

# Part I: The Fork in the Path
print("Part I: The Fork in the Path")
print("As you venture deeper, you come across a fork in the path.")
choice = input("Do you take the left path or the right path? ")

if choice.lower() == "left":
    print("You took the left path, which seems safe.")
    sys.exit()  # Stops the game

elif choice.lower() == "right":
    print("You took the right path, which is overgrown and mysterious.")

    # Continuation for the right path
    print("After traveling for a while, you come across a small, dilapidated hut.")
    choice = input("Do you want to enter the hut or do you want to keep continue down the path? ")

    if choice.lower() == "enter":
        print("You entered the hut and found a magical artifact.")
        # Continue the story from here
    elif choice.lower() == "continue":
        print("You continued down the path and encountered a talking tree.")

        # The Talking Tree
        print("A massive tree with a face carved into its trunk suddenly speaks to you.")
        choice = input("Choice 1: Ask the tree for guidance.\nChoice 2: Demand to know who it is.\nChoice 3: Ignore the tree and walk away.\nWhat do you choose? ")

        if choice == "1":
            print("You ask the tree for guidance. It gives you wise advice about the forest.")
            # Continue the story from here
        elif choice == "2":
            print("You demand to know who it is. The tree tells you it is the guardian of the forest.")
            # Continue the story from here
        elif choice == "3":
            print("You ignore the tree and walk away. The tree seems sad but lets you go.")
            # Continue the story from here
        else:
            print("Invalid choice. Please restart the game and choose again.")

        # Part III: The Enchanted River
        print("Part III: The Enchanted River")
        print("You reach a shimmering river that seems to hum with magical energy.")
        choice = input("Choice 1: Drink from the river.\nChoice 2: Cross the river using a fallen log.\nChoice 3: Follow the river upstream.\nWhat do you choose? ")

        if choice == "1":
            print("You drink from the river and feel a surge of magical energy. You now have the power to heal.")
            # Continue the story from here
        elif choice == "2":
            print("You carefully cross the river using a fallen log and continue your journey.")
            # Continue the story from here
        elif choice == "3":
            print("You follow the river upstream and discover a hidden waterfall with a secret cave behind it.")
            # Continue the story from here
        else:
            print("Invalid choice. Please restart the game and choose again.")

        # Part IV: The Dragon’s Lair
        print("Part IV: The Dragon’s Lair")
        print("You stumble upon the entrance to a cave, and you hear the sound of a dragon inside.")
        choice = input("Choice 1: Enter the cave to confront the dragon.\nChoice 2: Sneak around to find another way in.\nChoice 3: Retreat and find a safer route.\nWhat do you choose? ")

        if choice == "1":
            print("You enter the cave to confront the dragon. It is a fierce battle.")
            battle_choice = input("Choice 1: Fight bravely.\nChoice 2: Use the magical artifact.\nWhat do you choose? ")
            if battle_choice == "1":
                print("You fight bravely but are overpowered by the dragon.")
                print("The Dragon's Wrath: You confront the dragon but are overpowered. Your adventure ends tragically.")
            elif battle_choice == "2":
                print("You use the magical artifact and defeat the dragon.")
                print("The Treasure of the Forest: Your choices lead you to a hidden treasure trove guarded by friendly forest spirits. You become rich and famous.")
            else:
                print("Invalid choice. Please restart the game and choose again.")
        elif choice == "2":
            print("You sneak around to find another way in. You find a hidden entrance that leads to the dragon's treasure hoard.")
            print("The Treasure of the Forest: Your choices lead you to a hidden treasure trove guarded by friendly forest spirits. You become rich and famous.")
        elif choice == "3":
            print("You retreat and find a safer route. On your way back, you discover a hidden path that leads to a peaceful meadow.")
            print("The Escape: You manage to navigate the dangers and mysteries of the forest and return home safely, with a story to tell.")
        else:
            print("Invalid choice. Please restart the game and choose again.")

    else:
        print("Invalid choice. Please restart the game and choose again.")
else:
    print("Invalid choice. Please restart the game and choose again.")
