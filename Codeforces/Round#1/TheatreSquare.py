import math
n,m,a = map(int, input().split()) # input three positive integers
l = math.ceil(n/a) # side A
b = math.ceil(m/a) # side B
flags = l+b # total number of flags required
print(flags) # printing the output to the console
