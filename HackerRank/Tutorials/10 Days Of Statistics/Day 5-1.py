# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def poisson(mean, x):
    return ((mean**x)*math.exp(-mean))/math.factorial(x)
    
mean = float(input())
x = int(input())
p = poisson(mean,x)
print(p)
