#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import permutations

"""
L shape movement (a, b):
x2 = x1 +- a, y2 = y1 +- b,
x2 = x1 +- b, y2 = y1 +- a.

Each pair for 1 <= a, b < n, find minimum moves from (0,0) to (n-1,n-1),
if not possible, return -1.

Constraints: 5 <= n <= 25
Input: integer n
Output: n-1 lines with each n-1 elements with the corresponding no of moves

Input: n = 3
Possible moves: (1,1) (1,2)
                (2,1) (2,2)
Output: 2 -1
        -1 -1
        
Input: n = 5
Possible moves: (1,1) (1,2) (1,3) (1,4)
                (2,1) (2,2) (2,3) (2,4)
                (3,1) (3,2) (3,3) (3,4)
                (4,1) (4,2) (4,3) (4,4)
Output: 4 4 2 8
        4 2 4 4 
        2 4 -1 -1
        8 4 -1 1   
        
Notes:
- if (3,4) does not work, then (4,3) should not work too (symmetric board)   
- last permutation should never work
- check if multiples of (a,b) are dividable by dimension of board 
"""

# TODO: implement checkMovement function.
def checkMovement(move):
    return

# TODO: implement knighlOnAChessboard function.
def knightlOnAChessboard(n):
    lst = [i for i in range(1, n)]
    for permutation in permutations(lst, 2):
        print(permutation)



if __name__ == '__main__':
    n = 5
    knightlOnAChessboard(n)
