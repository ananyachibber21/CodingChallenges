n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
I = N.intersection(B)
print(len(I))