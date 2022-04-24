#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W

def weightedMean(X, W):
    # Write your code here
    l = []
    for i in range(n):
        x = X[i]*W[i]
        l.append(x)
    print("{:.1f}".format(sum(l)/sum(W)))

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    weightedMean(vals, weights)
