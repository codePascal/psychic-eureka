"""
For any two strings of digits, A and B, we define F_A,B to be the sequence (A,B,AB,BAB,ABBAB,...) in which each term is the concatenation of the previous two.

Further, we define D_A,B(n) to be the nth digit in the first term of FA,B that contains at least n digits.

Example:

Let A=1415926535, B=8979323846. We wish to find D_A,B(35), say.

The first few terms of FA,B are:
1415926535 (len = 10, 9 @ 5)
8979323846 (len = 10)
14159265358979323846 (len = 20, 9 @ 5)
897932384614159265358979323846 (len = 30)
14159265358979323846897932384614159265358979323846 (len = 50, 9 @ 35)

Then D_A,B(35) is the 35th digit in the fifth term, which is 9.

Now we use for A the first 100 digits of π behind the decimal point:

14159265358979323846264338327950288419716939937510
58209749445923078164062862089986280348253421170679

and for B the next hundred digits:

82148086513282306647093844609550582231725359408128
48111745028410270193852110555964462294895493038196 .

Find ∑n = 0,1,...,17   10n× DA,B((127+19n)×7n) .
"""

def find_next(fn0, fn1, idx, i):
    fn2 = fn0 + fn1
    i += 1
    print(fn0, fn1, fn2)
    if fn2 >= idx:
        # Length of concatenated strings is longer than index
        backtrack_elements([fn0, fn1, fn2], idx, i)
    else:
        # Concatenate next item
        find_next(fn1, fn2, idx, i)


def backtrack_elements(fn, idx, i):
    print(fn[2], idx, i)

    # Backtrack last increment
    idx -= fn[0]
    fn = reverse_fibbonacci(fn)
    i -= 1
    print(fn[0], fn[1], fn[2], idx, i)

    while i > 1:
        # Backtrack until condition is fulfilled
        if fn0 >= idx:
            # Elem is in fn0-part of fn2, skip reducing index
            fn = reverse_fibbonacci(fn)
            print("Idx <= fn0", fn[0], fn[1], fn[2], idx, i)
        elif fn0 < idx:
            # Elem is in fn1-part of fn2, index is reduced too
            idx -= fn[0]
            fn = reverse_fibbonacci(fn)
            print("Idx > fn0", fn[0], fn[1], fn[2], idx, i)
        i -= 1

    print((triplet[0]+triplet[1])[idx-1])


def reverse_fibbonacci(fn):
        fn[2] -= fn[0]
        fn[1] = fn[0]
        fn[0] = fn[2] - fn[1]
        return fn


if __name__ == '__main__':
    # n = int(input())
    n = 1
    for _ in range(n):
        triplet = list(input().split())
        # Extract elements in list and assign to variable
        fn0 = len(triplet[0])
        fn1 = len(triplet[1])
        idx = int(triplet[2])
        if len(triplet[0]+triplet[1]) >= idx:
            # Condition already fulfilled with first two entries
            print((triplet[0]+triplet[1])[idx-1])
        else:
            # Do until conditon is fulfilled
            find_next(fn0, fn1, idx, 0)
