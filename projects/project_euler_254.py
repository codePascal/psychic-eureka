"""
Optimize for large numbers, i.e. for g(i>40).
best shot for g(40) = 0.2977259159088135 [s]

"""

import math
import time

start_time = time.time()

# f(n) => f(342) = 3! + 4! + 2! = 32
def calculateFactorialDigits(n):
    sum = 0
    for digit in [int(d) for d in str(n)]:
        sum += math.factorial(digit)
    return sum

# s(n) => s(32) = 3 + 2 = 5
def calculateSumDigits(n):
    digits = [int(d) for d in str(n)]
    return sum(digits)


def calculateSumGs(lst, large_number):
    result = 0
    for elem in lst:
        result += calculateSumDigits(elem)
    print(result % large_number)


#t = int(input())
t = 1
for _ in range(t):
    #nm = list(map(int, input().split()))
    nm = [40, 100000]
    lst = list()
    for i in range(1, nm[0]+1):
        n_min = 1
        while True:
            f_n = calculateFactorialDigits(n_min)
            sf_n = calculateSumDigits(f_n)
            if (sf_n == i):
                # print("g(%i) =" %i, n_min)
                lst.append(n_min)
                break
            else:
                n_min += 1
    calculateSumGs(lst, nm[1])

print(time.time()-start_time)
