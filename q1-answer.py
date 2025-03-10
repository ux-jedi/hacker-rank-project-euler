#!/bin/python3

import math
import os
import random
import re
import sys



def sum_of_multiples(n, x):
    k = (n - 1) // x
    return x * k * (k + 1) // 2

def compute_sum(n):
    return sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15)

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(compute_sum(n))

# Count how many multiples of x exist below N: k=(N-1)//x
# Sum of the multiples: S_x = x * k * (k + 1) // 2
# Add up the sums of any multiple of 3 and 5, but avoid duplicated counts: S=S_3+S_5-S_15
