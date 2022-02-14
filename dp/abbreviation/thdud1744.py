
import math
import os
import random
import re
import sys
from itertools import groupby, islice

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

#   b e F g H 
# E x o x x x 
# F x x o x x 
# G x x x o x 
# ------------
#   0 1 1 1 0

#   A b C d E
# A o x x x x
# F x x x x x
# E x x x x o
# ------------
#   1 0 0 0 1

def abbreviation(a, b):
    # Write your code here
    b_len = len(b)
    a_len = len(a)
    if a == b:
        return "YES"
    table = [[0 for i in range(a_len)] for j in range(b_len)]
    for i in range(b_len):
        for j in range(a_len):
            if b[i] == a[j] or b[i] == a[j].upper():
                table[i][j] = 1
            else:
                table[i][j] = 0
    check = [0 for i in range(a_len)]
    for i in range(b_len):
        for j in range(a_len):
            if table[i][j] == 1:
                check[j] = 1
                break

    result = [i for i, j in groupby(check) if len(list(islice(j, 0, b_len))) == b_len]
    print(result)
    if result == [1]:
        return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        print(result)