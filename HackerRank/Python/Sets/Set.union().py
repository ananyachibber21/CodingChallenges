n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
U = N.union(B)
print(len(U))
