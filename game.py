import time

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
        print("You have chosen the", chosen_weapon + ".")
        print_with_typing("As you explore deeper into the dungeon, you encounter a group of menacing harpies.", delay=0.08)
        print_with_typing("You swing your", chosen_weapon, "at the harpies, but it's not effective enough.", delay=0.08)
        print_with_typing("The harpies overpower you, and you fall to your demise.", delay=0.08)
        print_with_typing("You died!")
        exit()
    else:
        print("You have chosen the", chosen_weapon + ".")
        print_with_typing("As you explore deeper into the dungeon, you hear the flapping wings of approaching harpies.")

        print_with_typing("The harpies are getting closer. What do you do?", delay=0.08)
        print("1. Shoot an arrow at them")
        print("2. Hide and wait for them to pass")
        print("3. Charge towards them with your bow")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print_with_typing("You draw your bow and shoot an arrow at the harpies.", delay=0.08)
            print_with_typing("The arrow finds its mark, striking down one of the harpies.", delay=0.08)
            print_with_typing("The remaining harpies scatter in fear, giving you an opportunity to escape.", delay=0.08)
            print("You successfully fend off the harpies with your bow and continue your journey.")
            break
        elif choice == "2":
            print_with_typing("You quickly find a hiding spot and wait for the harpies to pass.", delay=0.08)
            print_with_typing("The harpies fly by without noticing your presence.", delay=0.08)
            print("You emerge from your hiding spot and continue your journey undisturbed.")
            break
        elif choice == "3":
            print_with_typing("You bravely charge towards the harpies with your bow in hand.", delay=0.08)
            print_with_typing("Using your agility and skill, you manage to take down several harpies.", delay=0.08)
            print_with_typing("However, their numbers overwhelm you, and you are forced to retreat.", delay=0.08)
            print("You narrowly escape the harpies' clutches, wounded but alive.")
            break
        else:
            print("Invalid choice. Try again.")
            continue

    print()
    print("Congratulations, " + name + "! You have successfully dealt with the harpies and continue your adventure.")
