# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def binomial(n,x,p):
    return (math.factorial(n)/(math.factorial(n-x)*math.factorial(x)))*(p**x)*((1-p)**(n-x))

n, p = 10, 12/100
print(round(sum(binomial(n,x,p) for x in range(3)),3))
print(round(sum(binomial(n,x,p) for x in range(2, n+1)),3))
