import numpy

def arrays(arr):
    x = numpy.array(arr, float)
    return x[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
