magicians = ['alice', 'david', 'carolina']

for magician in magicians:
	print(f"I cannot wait to see your trick, {magician.title()}.")
	print(f"{magician.title()}, that was an amazing trick!\n")

print("Thank you everyone, that was a great show!\n")

pizzas = ['cheese', 'pepperoni', 'sausage']

for pizza in pizzas:
	print(f"I like {pizza} pizza")

print("I enjoy all types of pizzas\n")

animals = ['dog', 'cat', 'koala']

for animal in animals:
	print(f"A {animal} would be a great pet!")

print("Any of these animals would be a great pet\n")

for value in range(1,5): # off by one behavior, only prints 1-4
	print(value)

print("\n")
for value in range(1,6): # prints 1-5
	print(value)

print("\n")
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = [] # List of the first 10 square numbers
for value in range(1,11): # create a range from 1-11, so that it goes from 1-10 because of off by one behavior
	squares.append(value**2) # square the value and append to the list 

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(digits)

print("Min:", min(digits))
print("Max:", max(digits))
print("Sum:", sum(digits))

odd_squares = [index**2 for index in range(1, 11, 2)]
print(odd_squares)

print('\n')
for num in range(1,21):
	print(num)

million = list(range(1,1000001))
print("Min:",min(million))
print("Max:",max(million))
print("Sum from 1 to 1,000,000:", sum(million))

print('\n')
odd_num = list(range(1,21,2))
for temp in odd_num:
	print(temp)

print('\n')
print("Numbers from 1-30 divisible by 3: \n")
div3 = []
for h in range(1,31):
	if (h % 3 == 0):
		div3.append(h)

print(div3)

cubes = [index**3 for index in range(1,11)] # List comprehension for first 10 cubes
print("List of first 10 cubes:\n")
for cube in cubes:
	print(cube)

# Slicing
players = ["jacob", "lexi", "justin", "martha", "meghan"]
print(players[0:3]) # only prints players index 0-3
print(players[:4]) # if you omit the first number, python automatically starts at the beginning of the list
print(players[2:]) # if you omit the second number, python automatically traverses to the end of the list
print(players[-3:]) # if you use a negative number, it prints that many backwards from the end of the list
print("Here are the first three players on the team:")
for player in players[:3]:
	print(player.title())

my_foods = ['pizza', 'chicken', 'rice']
friend_foods = my_foods[:]
print("My favorite foods are:", my_foods)
print("My friends favorite foods are:", friend_foods)
my_foods.append('cake')
friend_foods.append('pie')
print("My favorite foods are:", my_foods)
print("My friends favorite foods are:", friend_foods)


print("The first two items in the list are:")
drinks = ['strawberry acai', 'sprite', 'coke', 'lemonade', 'pepsi', 'dr pepper']
for drink in drinks[:2]:
	print(drink)

print("The drinks in the middle of the list are:")
for drink in drinks[2:4]:
	print(drink)

print("The drinks at the end of the list are:")
for drink in drinks[4:]:
	print(drink)


