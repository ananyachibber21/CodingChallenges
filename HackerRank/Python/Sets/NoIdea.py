n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
x = 0
for i in arr:
    if(i in A):
        x = x + 1
    elif(i in B):
        x = x - 1
    else:
        continue
print(x)
