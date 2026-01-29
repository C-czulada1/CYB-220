#5-1
color = ('pink')
print("Is color == 'pink'? I think true")
print(color == 'pink')
print("Is color == 'black'? I think false")
print(color == 'black')
food = 'meatballs'
print("Is food == 'meatballs'? I think true")
print(food == 'meatballs')
print("Is food == 'hotdog'? I think false")
print(food == 'hotdog')
sport = 'hockey'
print("Is sport == 'hockey'? I think true")
print(sport == 'hockey')
print("Is sport == 'basketball'? I think false")
print(sport == 'basketball')
gaming = 'desktop'
print("Is gaming == 'desktop'? I think true")
print(gaming == 'desktop')
print("Is gaming == 'xbox'? I think false")
print(gaming == 'xbox')
clothing = 'sweatshirt'
print("Is clothing == 'sweatshirt'? I think true")
print(clothing == 'sweatshirt')
print("Is clothing == 'pants'? I think false")
print(clothing == 'pants')

#5-2
clothing = ['pants', 'hoodie', 'shirt', 'hat', 'socks']
if 'socks' in clothing:
    print("Socks is in the list")
else: print("Socks is not in the list")
if 'shirt' in clothing:
    print("Shirt is in the list")
else: print("Shirt is not in the list")
if 'hat' in clothing:
    print("Hat is in the list")
else: print("Hat is not in the list")
if 'pants' in clothing:
    print("Pants is in the list")
else: print("Pants is not in the list")
if 'hoodie' in clothing:
    print("Hoodie is in the list")
else: print("Hoodie is not in the list")
if 'shoes' in clothing:
    print("shoes are in the list")
else: print("Shoes are not in the list")

#5-3
alien_color = 'green'
if alien_color == 'green':
    print('You earned 5 points')

alien_color = 'red'
if alien_color == 'green':
    print('You earned 5 points')

#5-4
alien_color = 'green'
if alien_color == 'green':
    print('You earned 5 points')
else:
    print('You earned 10 points')

alien_color = 'yellow'
if alien_color == 'green':
    print('You earned 5 points')
else:
    print('You earned 10 points')

#5-5
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

#5-6
age = 27
if age < 2:
    print("This person is a baby")
elif age < 4:
    print("This person is a toddler")
elif age < 13:
    print("This person is a kid")
elif age < 20:
    print("This person is a teenager")
elif age < 65:
    print("This person is an adult")
else:
    print("This person is an elder")

#5-7
favorite_fruits = ['apple', 'pear', 'banana']
if 'apple' in favorite_fruits:
    print("You really like apples")
if 'pear' in favorite_fruits:
    print("You really like pears")
if 'banana' in favorite_fruits:
    print("You really like bananas")
if 'orange' in favorite_fruits:
    print("You really like oranges")
if 'grape' in favorite_fruits:
    print("You really like grapes")

#5-8
usernames = ['admin', 'chris', 'aj', 'bobby', 'radyn']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again!")

#5-9
usernames = []
if not usernames:
    print("We need to find some users!")
    
#5-10
current_users = ['Thomas', 'Frank', 'John', 'Ryan', 'Adam']
new_users = ['mark', 'susie', 'john', 'joey', 'adam']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

#5-11
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

