import numpy
arr = []
N, M = map(int, input().split())
for i in range(N):
    x = list(map(int,input().split()))
    arr.append(x)
m = numpy.min(arr, axis = 1)
print(m.max())
