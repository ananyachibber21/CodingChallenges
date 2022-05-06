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
