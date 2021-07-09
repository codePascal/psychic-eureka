"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers a < b < c, for which

    a^2 + b^2 = c^2

E.g. 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product of triplet (a, b, c).

https://projecteuler.net/problem=9

Correct answer: 31875000
"""


def is_pythagorean_triplet(triplet):
    return (triplet[0] * triplet[0] + triplet[1] * triplet[1]) == (triplet[2] * triplet[2])


def triplet_sum(triplet):
    return triplet[0] + triplet[1] + triplet[2]


def triplet_prod(triplet):
    return triplet[0] * triplet[1] * triplet[2]


# Pseudo
# minimum of a is 1, hence minimum of b is 2 (b > a) and therefore maximum of
# c is 1000 - 2 - 1 = 997
# fix c at end n, start with b at n-1 and start with a at 1
# check if numbers are a Pythagorean triplet, if so, check the sum otherwise
# check if the sum is larger or smaller than the goal, if larger, reduce b,
# if smaller, increase a
# at some point b and a meet, reduce c by 1, initialize iterators as at start

# generate numbers from 1 to 997
goal_sum = 1000
a_min = 1
b_min = a_min + 1
c_max = goal_sum - a_min - b_min
numbers = [i for i in range(a_min, c_max + 1)]
n = len(numbers)

# start iteration
c_it = n - 1
b_it = c_it - 1
a_it = 0
while True:
    # check if a and b are not equal, otherwise start iteration with decreased c
    if a_it >= b_it and c_it > 3:
        c_it -= 1
        b_it = c_it - 1
        a_it = 0

    # triplet with a, b, c
    triplet = (numbers[a_it], numbers[b_it], numbers[c_it])

    # check the sum of the triplet is equal the goal
    if triplet_sum(triplet) == goal_sum:
        # check if triplet is also a Pythagorean triplet
        if is_pythagorean_triplet(triplet):
            print('Project euler 9:', triplet_prod(triplet))
            break
        # the sum is correct but its not a Pythagorean triplet
        else:
            b_it -= 1
            a_it += 1
    # if the triplet sum is larger than goal, reduce b
    elif triplet_sum(triplet) > goal_sum:
        b_it -= 1
    # if the triplet sum is smaller than goal, increase a
    elif triplet_sum(triplet) < goal_sum:
        a_it += 1
    else:
        print('No Pythagorean triplet found')
        break
