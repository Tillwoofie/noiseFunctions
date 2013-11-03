#!/opt/local/bin/python3.3

import sys
import math

def list_primes(minval, maxval):
    primes = []
    for x in range(minval, maxval):
        if test_primality(x):
            primes.append(x)
    return primes
    
def test_primality(x):
    limit = math.ceil(math.sqrt(x))
    for val in range(2,limit+1):
        if x % val == 0:
            return False
    return True

if __name__ == '__main__':
    if len(sys.argv) == 2:
        primes = list_primes(1, int(sys.argv[1]))
    elif len(sys.argv) == 3:
        primes = list_primes(int(sys.argv[1]), int(sys.argv[2]))
    else:
        print("you bad...")
        exit(1)
    print(primes)
