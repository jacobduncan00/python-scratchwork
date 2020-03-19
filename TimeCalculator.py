input_seconds = float(input("Enter # of seconds: "))
hours = input_seconds // 3600
minutes = (input_seconds // 60) % 60
seconds = input_seconds % 60
print('')
print('Hours   :', hours)
print('Minutes :', minutes)
print('Seconds :', seconds) 
