# Used for 
# - Organizing mini databases
# - Very fast

dictionary = {'Jacob':1, 'Blaine':2, 'Justin':3}

# How you index into a dictionary
print(dictionary.get('Jacob'))
# Or
print(dictionary['Jacob'])

contacts = {
    'Jacob': {'Phone Number:':'850-582-9363', 'Email Address':'jacobduncan00@yahoo.com'},
    'Justin': {'Phone Number:':'777-888-9999', 'Email Address':'justinventura@salisbury.com'},
    'Blaine': {'Phone Number:':'111-222-3333', 'Email Address':'blainemason@salisbury.com'},
}

for contact, info in contacts.items():
    print('Contact List:' + 'Name' + contact + info)

