from math import isqrt
def isprime(num):
    '''
    Checks for primality of a number
    input: any real integer
    output: bool
    '''
    if num <= 3:
        return num > 1
    if num % 2 == 0  or num % 3 == 0:
        return False
    limit = isqrt(num)+1
    for i in range(2,limit,6):
        if num % i == 0 or num % (i+2):
            return False
    return True
