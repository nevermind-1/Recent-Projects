"""Factor Finder, by Ajuba okwuchukwu Anthony
Find all the factors of a number.
View this code at  ajubaokwuchukwuanthony2000@gmail.com
Tags:tiny beginner,math
"""

import math,sys

print('''Factor Finder,  by Ajuba Okwuchukwu Anthony
I believe you know what a prime number is
Let's discover some!''')

while True:
    print('Enter a postive whole number to factor (or QUIT):')
    response = input('> ')
    if response.upper() == 'QUIT':
        sys.exit()
    
    if not (response.isdecimal() and int(response) > 0):
        continue
    number = int(response)

    factors =  []

    # Find the factors of number:
    for j in range(1,int(math.sqrt(number)) + 1):
        if number % j == 0:
            factors.append(j)
            factors.append(number//j)
    #convert to a set to get rid of duplicate factors
    factors = sorted(list(set(factors)))

    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(', '.join(factors))




    
     