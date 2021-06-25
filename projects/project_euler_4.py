"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=4

Correct answer: 906609
"""
import numpy as np
from itertools import combinations_with_replacement


def is_palindromic(n):
    """ Returns if number is palindromic. """
    n_list = [int(i) for i in str(n)]
    return n_list == n_list[::-1]


# bruteforce approach: start with largest 3-digit number, create all possible multiplications, sort and
# iterate backwards until found
largest = 999

# create list of numbers 100 to largest
m = np.linspace(100, largest, largest-100+1)

# create combinations of two numbers, without doubles
comb = list(combinations_with_replacement(m, 2))

# create multiplications of each combination and sort in descending order
mult = list()
for tup in comb:
    mult.append(int(tup[0] * tup[1]))
mult_sorted = sorted(mult, reverse=True)

# iterate until found
i = 0
while True:
    if is_palindromic(mult_sorted[i]):
        print('Project euler 4:', mult_sorted[i])
        break
    elif i == len(mult_sorted) - 1:
        print('No palindromic found')
        break
    else:
        i += 1
