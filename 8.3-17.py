#8-3
def make_shirt(size, message):
    print(f"The shirt size is {size}, and the message is {message}")
    print()
make_shirt("Small", "I like video games")
make_shirt(size="Medium", message="Coding is fun!")

#8-4
def make_shirt(size= "Large", message= "I Love Python"):
    print(f"We are printing this shirt now")
    print(f"SIZE : {size}")
    print(f"MESSAGE : {message}")
    print()

make_shirt()
make_shirt(size="Medium", message="I Love Python")
make_shirt(size="Small", message="I also love Python too!")

#8-5
def describe_city(city, country):
    print(f"{city}, {country}")
    print()

describe_city(city="Boynton Beach" " is in", country="USA")
describe_city(city="Boston" " is in", country="USA")
describe_city(city="Moscow" " is in", country="Russia")

#8-6
def city_country(city, country):
    print(f"{city}, {country}")
    print()

city_country(city="Boston", country="USA")
city_country(city="Moscow", country="Russia")
city_country(city="Boynton Beach", country="USA")

#8-7
def make_album(artist, title, songs=None):
    album = {
        "Artist": artist,
        "Title": title,
    }

    if songs is not None:
        album["Songs"] = songs

    return album
album1 = make_album("Drake", "Scorpion")
album2 = make_album("Zach Bryan", "Elizabeth")
album3 = make_album("Sam Barber", "Music for the Soul", "8")
print(album1)
print(album2)
print(album3)
"""
#8-8
def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if songs is not None:
        album["songs"] = songs

    return album


print("Enter album information (type 'quit' at any time to stop).")

while True:
    artist = input("Artist name: ")
    if artist.lower() == "quit":
        break

    title = input("Album title: ")
    if title.lower() == "quit":
        break

    album = make_album(artist, title)
    print("Album created:", album)
"""
#8-9
messages = ["Hey, how are you?", "Don't forget to go to class!", "What are you doing later?"]
def show_messages(messages):
    for message in messages:
        print(message)
show_messages(messages)

#8-10
messages = ["Hey, how are you?", "Don't forget to go to class!", "What are you doing later?"]
sent_messages = []
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
send_messages(messages, sent_messages)
print("Remaining messages:", messages)
print("Sent messages:", sent_messages)

#8-11
messages = ["Hey, how are you?", "Don't forget to go to class!", "What are you doing later?"]
sent_messages = []
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
send_messages(messages[:], sent_messages)
print("Original messages:", messages)
print("Sent messages:", sent_messages)

#8-12
def make_sandwhich(*items):
    print("Sandwhich order:")
    for item in items:
        print("-", item)
    print()
make_sandwhich("turkey", "cheese")
make_sandwhich("bacon", "lettuce", "tomato")
make_sandwhich("ham", "lettuce", "mayo", "cheese")

#8-13
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info
user_profile = build_profile(
    "Chris",
    "Czulada",
    age=21,
    major="Criminal Justice and Cybersecurity",
    hobby="Gaming"
)
print(user_profile)

#8-14
def make_car(manufacturer, model, **car_info):
    car = {
        "manufacturer": manufacturer,
        "model": model,
    }
    for key, value in car_info.items():
        car[key] = value
    return car
car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)