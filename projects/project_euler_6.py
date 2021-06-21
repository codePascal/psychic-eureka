"""
Sum square difference

The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

https://projecteuler.net/problem=6

Correct answer: 25164150
"""

n = 100
sum_of_squares = sum([i*i for i in range(1, n+1)])
squares_of_sum = sum([i for i in range(1, n+1)]) ** 2
print('Project euler 6:', squares_of_sum - sum_of_squares)
