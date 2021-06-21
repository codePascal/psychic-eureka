"""
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

https://projecteuler.net/problem=5

Correct answer: 232792560
"""


def least_common_multiple(m, n):
    """ Computes least common multiple of two numbers. """
    # if one of the numbers if 0, lcm is 0
    if m == 0 or n == 0:
        return 0
    else:
        # check that m is smaller than n
        if m > n:
            m, n = n, m

        # use n as main counter, try if divisible by m
        n_counter = n
        while n_counter <= m * n:
            if n_counter % m == 0:
                return n_counter
            else:
                n_counter += n
        return m * n


# find lcm of previous lcm and next number
lcm = 1
for i in range(2, 20):
    tmp = least_common_multiple(lcm, i)
    lcm = tmp
print('Project euler 5:', lcm)
