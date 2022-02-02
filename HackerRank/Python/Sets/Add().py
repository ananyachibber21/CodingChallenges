N = int(input())
list1 = []
for i in range(N):
    country = input()
    list1.append(country)
set1 = set(list1)
print(len(set1))
