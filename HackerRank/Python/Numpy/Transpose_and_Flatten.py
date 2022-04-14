import numpy as np
N, M = map(int, input().split())
list1 = []
for i in range(N):
        x = list(map(int, input().split()))
        list1.append(x)
arr = np.array(list1)
a = arr.transpose()
print(a)
b = arr.flatten()
print(b)


