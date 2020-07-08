#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations_with_replacement, product

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
                  -   (2,2)
Output: 2 -1
        -1 -1

Input: n = 5
Possible moves: (1,1) (1,2) (1,3) (1,4)
                  -   (2,2) (2,3) (2,4)
                  -     -   (3,3) (3,4)
                  -     -     -   (4,4)
Output: 4 4 2 8
        4 2 4 4 
        2 4 -1 -1
        8 4 -1 1   

Notes:
- if (3,4) does not work, then (4,3) should not work too (symmetric board) 
- same if move works => output matrix is symmetric  
- check if multiples of (a,b) are dividable by dimension of board 
"""


# TODO: implement checkMovement function.
# Function should take movement parameters and check if possible to move towards (n-1,n-1).
def checkMovement(move):
    return


# TODO: implement knighlOnAChessboard function.
# Function creates all possible movements and calls function to check feasibiliy.
def knightlOnAChessboard(n):
    lst = [i for i in range(1, n)]
    #for move in product(lst, repeat=2)
    for move in combinations_with_replacement(lst, 2):


if __name__ == '__main__':
    n = 5
    knightlOnAChessboard(n)
