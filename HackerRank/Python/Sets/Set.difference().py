n = int(input())
N = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
D = N.difference(B)
print(len(D))