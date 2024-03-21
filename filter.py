numbers = list(i for i in range(0, 11))

'''
def prime(x):
    if x%2 == 1:
        return x

primeNumbers = list(filter(prime, numbers))
'''

primeNumbers = list(filter(lambda x: x%2==1, numbers))

print(primeNumbers)