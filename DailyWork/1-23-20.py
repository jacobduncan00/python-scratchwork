users = ['jacob', 'ben', 'lexi', 'admin']

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again")
else:
    print("No users found in the list!")

current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['newuser1', 'user2', 'newuser3', 'user4', 'newuser5']

for new_user in new_users:
    if new_user in current_users:
        print("Username has already been used!")
    else:
        print(f"Welcome new user: {new_user.title()}")

alien_0 = {'color' : 'green', 'points' : 5}
pcolor = alien_0['color']
ppoints = alien_0['points']
print(f"The {pcolor} alien just earned {ppoints} points!")
alien_0['xposition'] = 0
alien_0['yposition'] = 25
print(alien_0)
print(f"The alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

favorite_languages = {
    'me' : 'python',
    'lexi' : 'c',
    'sarah' : 'ruby',
    'justin' : 'c++',
}

print(f"Sarah's favorite language is {favorite_languages['sarah']}")

user_o = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

for key, value in user_o.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

