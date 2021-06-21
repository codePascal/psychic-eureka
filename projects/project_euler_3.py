"""
Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3

Correct answer:
"""


def is_prime(n):
    # if integer is a prime, then list is empty
    if not [i for i in range(2, n) if n % i == 0]:
        return True
    return False


# define number
n = 600851475143

# find divisors for number n, divisor 1 and even divisors are not considered
odd_divisors = [i for i in range(n, 3, -2) if n % i == 0]

# loop through possible divisors, if prime is found break
i = 0
while True:
    if i == len(odd_divisors) - 1:
        print('No prime found!')
        break
    elif is_prime(odd_divisors[i]):
        print('Project euler 3:', odd_divisors[i])
        break
    else:
        i += 1
