# Enter your code here. Read input from STDIN. Print output to STDOUT

# x,y=map(float,input().split())
# print(format(160+40*(x+x**2),'.3f'))
# print(format(128+40*(y+y**2),'.3f'))

x,y=map(float,input().split())
print(round(160+40*(x+x**2),3))
print(round(128+40*(y+y**2),3))
