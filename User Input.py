
#1
name = input("Enter your name: ")
print(f"Welcome to Anderson University, {name.title()}!")

#2
money = int(input("How much money do you have to spend on a processor? $: "))
i3_price = 150
i5_price = 200
i7_price = 400
i9_price = 600
if money >= i9_price:
    print("You can afford an i9 processor.")
elif money >= i7_price:
    print("You can afford an i7 processor.")
elif money >= i5_price:
    print("You can afford an i5 processor.")
elif money >= i3_price:
    print("You can afford an i3 processor.")
else:
    print("You can not afford a processor.")

#3

while True:
    user_input = input("Enter an integer (or type 'stop' to quit: ")
    if user_input.lower() == 'stop':
        print("Program ended")
        break

    number = int(user_input)
    if number % 2 == 0:
        print("That number is even.\n")
    else:
        print("That number is odd.\n")


#4
prompt = "\nPlease enter the name of your favorite vehicle brand:"
prompt += "\n(Enter 'quit' to stop):"
active = True
while active:
    brand = input(prompt)
    if brand == 'quit':
        active = False
        break
    else:
        print("My favorite vehicle brand is brand}.")

#5
ubuntu_flavors = {'edubuntu', 'kubuntu', 'lubuntu', 'ubuntu budgie', 'ubuntu cinnamon', 'ubuntu kylin'}
poll = {}

active = True
while active:
    print("Available Flavors")
    for flavors in ubuntu_flavors:
        print(flavors)
    user = input("Enter a username or type 'quit' to stop: ")
    if user == 'quit':
        active = False
        print("End of poll")
        break
    flavor = input("What is your favorite flavor of ubuntu? ")
    if flavor in ubuntu_flavors:
        poll[user] = flavor
        print(f"Thank you {user} you favorite {flavor} has been recorded")
    else:
        print(f"Sorry, {user} {flavor} is not a valid flavor.")
        print(f"Please refer to the flavors previously stated")
print("")
print(f"Your poll results {poll}")
