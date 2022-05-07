#!/bin/python3

import math
import os
import random
import re
import sys
import statistics as st

# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    new = []
    for i in range(len(values)):
        for j in range(freqs[i]):
            new.append(values[i])
    s = sorted(new)
    
    if len(s)%2 != 0:
       q1 = st.median(s[:len(s)//2])
       q3 = st.median(s[len(s)//2+1:])
    else:
       q1 = st.median(s[:len(s)//2])
       q3 = st.median(s[len(s)//2:])
    
    iqr = q3-q1
    print("{:.1f}".format(iqr))    
  
if __name__ == '__main__':
    n = int(input().strip())
    val = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().rstrip().split()))
    interQuartile(val, freq)

    
