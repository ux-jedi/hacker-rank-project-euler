# Find the largest prime factor of N

#!/bin/python3

import sys
import math

def largest_prime_factor(n):
    while n % 2 == 0:
        max_prime = 2
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i

  if n > 2:
        max_prime = n

    return max_prime

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        print(largest_prime_factor(n))


# Remove all factors of 2
# Check for odd factors, starting at 3 to sq.root of N.
