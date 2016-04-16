from math import sqrt; from itertools import count, islice

def checkIfJamCoin():
    # Check if non prime in Base 2
    # Check if non prime in Base 3
    # Check if non prime in Base 4
    # Check if non prime in Base 5
    # Check if non prime in Base 6
    # Check if non prime in Base 7
    # Check if non prime in Base 8
    # Check if non prime in Base 9
    # Check if non prime in Base 10
    pass

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

