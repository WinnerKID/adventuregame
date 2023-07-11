import time

# typing delay
def print_with_typing(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

while True:
    name = input("Enter your name: ").capitalize()
    if len(name) < 4:
        print("Name should be at least 4 characters long. Try again.")
    else:
        break

print("Welcome, " + name)
print()
print(''' /\_/\  
( o.o ) 
 > ^ <
''')

print_with_typing("----------------------------------------", delay=0.09)
weapons = ["sword", "bow", "staff"]

while True:
    print("Choose your weapon:")
    for i, weapon in enumerate(weapons, 1):
        print(f"{i}. {weapon}")
    weapon_choice = input("Enter the number corresponding to your chosen weapon: ")

    if not weapon_choice.isdigit() or int(weapon_choice) not in range(1, len(weapons) + 1):
        print("Invalid choice. Try again.")
        continue

    chosen_weapon = weapons[int(weapon_choice) - 1]
    if chosen_weapon != "bow":
        print("You have chosen the " + chosen_weapon + ".")
        print()
        print_with_typing("As you explore deeper into the dungeon, you encounter a group of menacing harpies.\n"
                          +"You swing your " + chosen_weapon + " at the harpies, but it's not effective enough.\n"
                          "The harpies overpower you, and you fall to your demise.")
        print("")
        print_with_typing("You died!")
        exit()
    else:
        print("You have chosen the " + chosen_weapon + ".")
        print()
        print("1. Shoot an arrow at them")
        print("2. Hide and wait for them to pass")
        print("3. Charge towards them with your bow")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print()
            print_with_typing("You draw your bow and shoot an arrow at the harpies.\n"
                              "The arrow finds its mark, striking down one of the harpies.\n"
                              "The remaining harpies scatter in fear, giving you an opportunity to escape.")
            print("")
            print("You successfully fend off the harpies with your bow and continue your journey.")
            print()
            print_with_typing("As you walk further down the dungeon, you find a big gate.\nYou can feel a powerful energy behind the doors. ")
            print()

            # Prompt user to type "OPEN" to open the gate
            while True:
                open_input = input("Type OPEN to open the gate: ").upper()
                if open_input != "OPEN":
                    print_with_typing("You have no choice " + name)
                else:
                    print_with_typing("\nThe gate opens, revealing a hidden path.")
                    break
            break

        elif choice == "2":
            print()
            print_with_typing("You quickly find a hiding spot and wait for the harpies to pass.\n"
                              "The harpies fly by without noticing your presence.\n")
            print()
            print("You emerge from your hiding spot and continue your journey undisturbed.")
            print()
            print_with_typing("As you walk further down the dungeon, you find a big gate.\nYou can feel a powerful energy behind the doors. ")
            print()

            # Prompt user to type "OPEN" to open the gate
            while True:
                open_input = input("Type OPEN to open the gate: ").upper()
                if open_input != "OPEN":
                    print_with_typing("You have no choice " + name)
                else:
                    print_with_typing("\nThe gate opens, revealing a hidden path.")
                    break
            break

        elif choice == "3":
            print()
            print_with_typing("You bravely charge towards the harpies with your bow in hand.\n"
                              "Using your agility and skill, you manage to take down several harpies.\n"
                              "However, their numbers overwhelm you, and you are forced to retreat.")
            print("")
            print_with_typing("As the harpies surround you, their talons tear through your defenses.\n"
                              "You fight valiantly but succumb to your injuries, unable to escape their grasp.")
            exit()
        else:
            print("Invalid choice. Try again.")
            continue


print("~You look around the room and see a lady with a big hat in the middle of the room.~")
