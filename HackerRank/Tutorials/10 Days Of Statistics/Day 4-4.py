# Enter your code here. Read input from STDIN. Print output to STDOUT

def geometric(p,q,i):
    return ((q**(i-1))*p)

p1, p2 = map(int, input().split())
x = int(input())
p = p1/p2
q = 1-p
g = 0
for i in range(1,x+1):
    g = g + geometric(p,q,i)
print(round(g,3))
