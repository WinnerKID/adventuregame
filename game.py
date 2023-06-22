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
    break

print("You have chosen the", chosen_weapon + ".")
print()
print("As you explore deeper into the dungeon, you encounter a group of menacing creatures.")

while True:
    print("Choose a number from 1 to 10, " + name)
    number_input = input("Number: ")

    if not number_input.isdigit():
        print("That's not a number, DIE!")
        continue

    number = int(number_input)

    if number == 5:
        print("CORRECT, " + name)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("You grab your", chosen_weapon, "and swiftly run towards the creatures, ready to battle them.")
        time.sleep(2)
        print("With each swing of your weapon, you fight valiantly, defeating the creatures one by one.")
        time.sleep(2)
        print("As the last creature falls, you catch your breath and feel a sense of accomplishment.")
        break
    else:
        print("YOU DIED, " + name)

print()
print("You have emerged victorious, " + name + "! Your bravery and skill have triumphed in the dungeon.")
