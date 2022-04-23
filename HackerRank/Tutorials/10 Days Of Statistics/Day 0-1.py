import statistics
N = int(input())
X = list(map(int, input().split()))
# mean
print("{:.1f}".format(sum(X)/len(X)))
s = sorted(X)
#median
if(N%2==0):
    m1 = int((N/2)-1)# Since the indexing starts from zero
    m2 = int(N/2)
    median = (s[m1] + s[m2])/2
else:
    m = int(((N+1)/2)-1)
    median = s[m]
print("{:.1f}".format(median))
#mode
# l1 = []
# for i in range(0, s+1):
#     l1.append(s.count(i))
print(statistics.mode(s))
