"""
10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?

https://projecteuler.net/problem=7

Correct answer: 104743
"""


def is_prime(n):
    # if integer is a prime, then list is empty
    if not [i for i in range(3, n, 2) if n % i == 0]:
        return True
    return False


# find this prime number
prime_search = 10001

# initialize loop, 2 is already found as prime
prime_count = 1
n_count = 3
while True:
    # increment prime counter
    if is_prime(n_count):
        prime_count += 1

    # print and break the loop
    if prime_count == prime_search:
        print('Project euler 7:', n_count)
        break

    # increment number counter by two, even numbers not considered
    n_count += 2
