# Calculate the sum of even Fibonacci numners below or equal to N.

#!/bin/python3

import sys

def sum_even_fibonacci(n):
    a, b = 2, 8
    sum_even = 2

    while b <= n:
        sum_even += b
        a, b = b, 4 * b + a
    return sum_even

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        print(sum_even_fibonacci(n))

# Formula for even Fibonacci numbers: E_n = 4 * E_n-1 + E_n-2
