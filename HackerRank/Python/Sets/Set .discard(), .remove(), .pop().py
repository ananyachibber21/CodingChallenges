n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    x, *y = map(str, input().split())
    getattr(s,x)(*(int(k) for k in y))
print(sum(s))
