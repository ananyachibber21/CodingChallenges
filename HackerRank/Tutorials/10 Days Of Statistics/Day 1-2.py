from statistics import median
N,arr = int(input()),[]
data,freq = list(map(int,input().split())),list(map(int,input().split()))
for i in range(N):
        arr += [data[i]] * freq[i]
arr.sort()
t = int(len(arr)/2)
if len(arr)%2==0:
        q1=arr[:t]
        q3=arr[t:]
else:
        q1=arr[:t]
        q3=arr[t+1:]
print(round(float(median(q3)-median(q1)), 1))

#or

import statistics as st
n = int(input())
X = [int(i) for i in input().split()]
F = [int(i) for i in input().split()]

S= []
for i in range(n):
    S.extend([X[i]]*F[i])

S = sorted(S)


n = len(S)
n2 = int(n/2)
print(round(float(st.median(S[-n2:])-st.median(S[:n2])),1))
