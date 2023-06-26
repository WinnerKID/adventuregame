import time

# typing delay
def print_with_typing(text, delay=0.1):
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

print_with_typing(". . .", delay=0.5)
