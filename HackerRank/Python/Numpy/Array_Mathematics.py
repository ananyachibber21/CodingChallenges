import numpy
N, M = map(int, input().split())
for i in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
A = numpy.array([a], int)
B = numpy.array([b], int)
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)

