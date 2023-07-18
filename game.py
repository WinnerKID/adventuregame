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
                              "The arrow finds its mark, striking down one of the monster.\n"
                              "The remaining foes scatter in fear, giving you an opportunity to escape.")
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


print_with_typing("You spot a lady with a big smile in the middle of the room")
print('''/////////////\\\\
(((((((((((((( \\\\
))) ~~      ~~  (((
((( (*)     (*) )))
)))     <       (((
((( '\______/`  )))
)))\___________/(((
       _) (_
      / \_/ \
     /(     )\
    // )___( \\
    \\(     )//
     (       )
      |  |  |
       | | |
       | | |
      _|_|_|_''')
print("")
print_with_typing("You walk closer towards her cautiously")
time.sleep(1)
print_with_typing("Her grin makes you feel a bit uneasy, making you strike a question at her\n")


while True:
    askher = input("Ask her who she is: ")

    if askher.strip() == "Who are you?":
        print_with_typing("I am the messenger.")
        time.sleep(1)
        print_with_typing("In your head: WELL THAT EXPLAINS NOTHING")
        break

    else:
        print_with_typing(". . .")
        continue

print("~Another question pops into your head~")

while True:
    whereami = input("Ask her where you are: ")

    if whereami.strip() == "Where am I?":
        print_with_typing("God's dungeon.")
        time.sleep(2)
        print_with_typing(f"{name}: Did god put me in here?")
        print_with_typing("Lady: . . .")
        break

    else:
        print_with_typing(". . .")
        continue

print_with_typing("~Dead silence in the room~")
time.sleep(2)

print_with_typing("She's of no use to you now.\rYou draw your bow out and shoot aiming at her head")
print("~SwwwoooOOOOsshhhHH~")
time.sleep(1)

print("It passed through her body...\n")
print_with_typing("Is she a ghost?\n")

print("~Her eyes stare back at you~")
print('''(⊙‿⊙)''')

print_with_typing("Freaked out, you pull out another arrow aiming for her head again\n")
print("Before you can even shoot")
time.sleep(1)
print_with_typing("She screams: RIIIIIAAAAAAAAAAAAAAAAIIIEEEEEEEEEEEHHHHHHH\n")
print("You immediately cover your ears due to the loud noise\r~It's too much for you to handle~\rYou collapse just as she finishes her loud shriek")



