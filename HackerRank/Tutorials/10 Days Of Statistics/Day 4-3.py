# Enter your code here. Read input from STDIN. Print output to STDOUT

p1, p2 = map(int, input().split())
x = int(input())
p = p1/p2
q = 1-p
g = (q**(x-1))*p
print(round(g,3))
