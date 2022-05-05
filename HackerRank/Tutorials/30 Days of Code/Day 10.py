remainder_list = []

while bn > 0:
    remainder = bn % 2
    bn = bn//2
    remainder_list.append(remainder)

count = 0
max_ = 0

for i in remainder_list:
    if i == 1:
        count += 1
        if max_ < count:
            max_ = count
    else:
        count = 0

return max_
if name == 'main': n = int(input().strip())

print(binary_numbers(n))
