def fibonacci_sequence(n):
    if n <= 1 or n == 2: #base case
        return 1

    return fibonacci_sequence(n-2) + fibonacci_sequence(n-1) # recursive part


#print(fibonacci_sequence(9))

def func(m,n):
    if n == 1:
        return m
    return func(m,n-1) * m

print(func(5,3))