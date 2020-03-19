dimensions = (200,50) # Tuple, a list that cannot be changed
print(dimensions[0])
print(dimensions[1])

# If we try to change a value of a tuple, we get an error
#dimensions[0] = 250	

for dimension in dimensions:
	print(dimension)

# To write over a tuple, we must change the dimension list
dimensions = (400,100)
for dimension in dimensions:
	print(dimension)

cars = ['audi', 'bmw', 'toyota', 'ford']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())	

print('\n')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")

user = 'andrew'

if user in banned_users:
	print(f"{user.title()}, you are banned and cannot post a response.")

age = 17

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40

print(f"Your admission cost is ${price}")



