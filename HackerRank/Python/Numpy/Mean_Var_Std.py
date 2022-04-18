import numpy
arr = []
N, M = map(int, input().split())
for i in range(N):
    x = list(map(int, input().split()))
    arr.append(x)
my_array = numpy.array(arr)
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None), 11))
