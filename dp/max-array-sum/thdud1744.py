#!/bin/python3

import math
import os
import random
import re
import sys

# 5
# 3 7 4 6 5
# max_sum
# 3 7 7 13 13

# 5
# -2 1 3 -4 5
# max_sum
# -2 1 3 3 8

    

def maxSubsetSum(arr):
# Note that any individual element is a subset as well.
# the case when all elements are negative, maximum sum is 0. 
    max_sum = [0 for i in range(n)]
    max_sum[0] = arr[0]
    max_sum[1] = max(arr[0], arr[1])
    for i in range(2, n):
        max_sum[i] = max(arr[i], arr[i]+max_sum[i-2], max_sum[i-1])
    return max_sum[-1]

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)
