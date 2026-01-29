pizzas = ['Cheese', 'Pepperoni','Meat Lovers']
for pizza in pizzas:
    print(pizza)
    print(f"I love to eat {pizza.title()} pizza")
print(f"I love to eat Cheese pizza")
print(f"I love to eat Pepperoni pizza")
print(f"I love to eat Meat Lovers pizza")

Animals = ['dog', 'cat', 'rabbit']
for animal in Animals:
    print(animal)
    print(f"A {animal.title()} has a lot of fur")
print(f"All of these animals are great household pets")

for value in range(1,21):
    print(value)

numbers = list(range(1,1_000_001))
for number in numbers:
    print(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)

multiples_of_three = list(range(3,31,3))
for number in multiples_of_three:
    print(number)

cubes = []
for number in range(1,11):
    cubes.append(number ** 3)
for cube in cubes:
    print(cube)

cubes = [number ** 3 for number in range(1,11)]
for cube in cubes:
    print(cube)

people = ['chris', 'radyn', 'frank', 'matty', 'bushnoe']
print("The first three people are:")
print(people[:3])
print("The last three people are:")
print(people[-3:])
print("The middle three people are:")
print(people[1:4])

pizzas = ['Cheese', 'Pepperoni','Meat Lovers']
friend_pizzas = pizzas[:]

pizzas.append('BBQ Chicken')
friend_pizzas.append('Veggie')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

foods = ('pizza', 'burgers', 'chicken', 'pasta', 'ice cream')
for food in foods:
    print(food)

print("\nRevised Menu")

foods = ('salad', 'burgers', 'chicken', 'pasta', 'shrimp')
for food in foods:
    print(food)
