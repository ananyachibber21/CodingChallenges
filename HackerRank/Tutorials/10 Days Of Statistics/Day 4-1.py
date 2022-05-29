# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
def binomial(n,x,p):
    return (math.factorial(n)/(math.factorial(n-x)*math.factorial(x)))*(p**x)*((1-p)**(n-x))

n, p = 6, 1.09/2.09 
b = 0
for x in range(3,7):
    b = b + binomial(n,x,p)
print(round(b,3))
