#1
person = {'f_name': 'Christopher', 'l_name':'Czulada', 'age':'21', 'hometown': 'Levittown', 'current_city': 'Boynton Beach', 'user': "C.Czulada1"}
print(person)

print(person['f_name'])
print(person['l_name'])
print(person['age'])
print(person['hometown'])
print(person['current_city'])
print(person['user'])

#2
print(f"This persons first name is {person['f_name']}, and their last name is {person['l_name']}, they are {person['age']} years old, and have the username {person['user']}")
print(f"They are originally from {person['hometown']}, and they currently live in {person['current_city']}")

#3
definitions = {
    "python": "A high-level programming language known for its readability and wide range of applications.",
    "variable": "A name that stores a value which can be changed during program execution.",
    "list": "A collection of items stored in a specific order that can be modified.",
    "method": "A function that is associated with an object and acts on its data.",
    "if statement": "A conditional statement that runs code only when a given condition is true.",
    "dictionary": "A collection of key-value pairs used to store related data.",
    "function": "A reusable block of code designed to perform a specific task."
}

print("Python:", definitions["python"], "\n")
print("Variable:", definitions["variable"], "\n")
print("List:", definitions["list"], "\n")
print("Method:", definitions["method"], "\n")
print("If Statement:", definitions["if statement"], "\n")
print("Dictionary:", definitions["dictionary"], "\n")
print("Function:", definitions["function"], "\n")

#4
for word, meaning in definitions.items():
    print(f"{word}: {meaning}\n")

#5
south_carolina_counties = {"Anderson County": "Anderson\n", "Calhoun County": "St. Matthews\n", "Florence County": "Florence\n", "Georgetown County": "Georgetown\n", "Pickens County": "Pickens\n"}
for county, seat in south_carolina_counties.items():
    print(f"{county}: {seat}")

#6
county_list = {"Greenville County": "Greenville\n", "Charleston County": "Charleston\n", "Richland County": "Columbia\n", "Horry County": "Conway\n"}
for county, seat in south_carolina_counties.items():
    if county in county_list:
        print(f"{county} is in our dictionary, and the seat is {south_carolina_counties[county]}")
    else:
        print(f"{county_list} is not in our dictionary. We will add this county shortly. Thanks!")

#7

charleston_county = {'Charleston': '150,227', 'North Charleston': '114,852', 'Mount Pleasant': '91,884', 'Summerville': '54,608', 'Folly Beach': '2,671'}
greenville_county ={'Greenville': '70,720', 'Greer': '33,842', 'Mauldin': '25,875', 'Simpsonville': '25,649', 'Taylors': '23,986'}
richland_county ={'Columbia': '137,541', 'Irmo': '12,042', 'Forest Acres': '10,558', 'Eastover': '800', 'Arcadia Lakes': '768'}
horry_county ={'Myrtle Beach': '37,958', 'Conway': '27,951', 'North Myrtle Beach': '18,901', 'Surfside Beach': '4,256', 'Aynor': '1,053'}
lexington_county ={'Lexington': '24,208', 'West Columbia': '17,870', 'Cayce': '13,740', 'Irmo': '12,042', 'Chapin': '1,791'}
for county in county_list:
    for city, population in county_list:
        print(f"In {county.title()}, the population is {population}")
#8
sc_counties = {
    'Charleston County': ['Charleston', 'North Charleston', 'Mount Pleasant'],
    'Richland County': ['Columbia', 'Irmo', 'Forest Acres'],
    'Greenville County': ['Greenville', 'Greer', 'Mauldin'],
    'Horry County': ['Myrtle Beach', 'Conway', 'North Myrtle Beach'],
    'York County': ['Rock Hill', 'Fort Mill', 'York'],
}
for county, seat in sc_counties.items():
    print(f"In {county}: the largest cities are {sc_counties[county]}")

