#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def quartiles(arr):
    # Write your code here
    if len(arr) % 2 == 0:
        return(arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2
    else:
        return arr[len(arr) // 2]

n = int(input().strip())
data = sorted(list(map(int, input().rstrip().split())))

if(len(data)%2==0):
    q2 = quartiles(data)
    q1 = quartiles(data[:len(data)//2])
    q3 = quartiles(data[len(data)//2:])
else:
    q2 = data[len(data) // 2]
    q1 = quartiles(data[:data.index(q2)])
    q3 = quartiles(data[data.index(q2)+1:])
print(q1, q2, q3, sep='\n')
