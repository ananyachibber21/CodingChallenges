n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
S = N.symmetric_difference(B)
print(len(S))
