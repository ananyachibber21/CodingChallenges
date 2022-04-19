import numpy
x = int(input())
A = numpy.array([list(map(int,input().split())) for i in range(x)])
B = numpy.array([list(map(int,input().split())) for i in range(x)])
print(numpy.dot(A,B))
