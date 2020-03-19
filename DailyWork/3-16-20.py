# Use // for integer division "not comments :/"
# Use ** for exponents

a = 5/2
print(a)
b = 5//2
print(b)
c = -5//2
print(c)

# Mathematical precedence
# 1. Exponentiation : **
# 2. Mult, div, mod: * / // %
# 3. Add, sub: + -

result = 12.0 + 6.0 / 3.0
print(result)

total_seconds = float(input('Enter a number of seconds: '))
hours = total_seconds // 3600
minutes = (total_seconds // 60) % 60
seconds = total_seconds % 60

print('Time in hours, minutes, and seconds:')
print('Hours:', hours)
print('Minutes:', minutes)
print('Seconds:', seconds)

# Printing with spaces in between
print('One', end=' ')
print('Two', end=' ')
print('Three')

# When multiple arguments are passed to the print function, they are
# automatically seperated by a space when they are displaytd on the screen

print('One', 'Two', 'Three')

# However you can make a seperator

print('One', 'Two', 'Three', sep='***')

# C++ \n works too!

print('One\nTwo\nThree\n')

# Character Guideline 

# \n next line
# \t next horizontal tab

print('Mon\tTues\tWed')
print('Thur\tFri\tSat')

# \' single quote print

print('I\'m ready to begin.')

# \" double quote print

print("Your assignment is to read \"Hamlet\" by tomorrow.")

# \\ backslash printed

print('The path is C:\\temp\\data.')

# String concatenation

print('This is ' + 'one string.')

# Formatting numbers
# Will format to 2 floating points

print(12345.6789)

print(format(12345.6789, '.2f'))

# Using designator!!! can put commas, apost, etc.

print(format(123456, ',d'))



