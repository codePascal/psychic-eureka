"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

# initialize Fibonacci sequence with first two elements
fibonacci = list()
fibonacci.append(1)
fibonacci.append(2)

# counter
i = 2

# create Fibonacci sequence until value exceeds 4 million
while True:
    if fibonacci[i - 2] + fibonacci[i - 1] < 4000000:
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
        i += 1
    else:
        break

# compute sum of even-valued terms
print(sum([i for i in fibonacci if i % 2 == 0]))