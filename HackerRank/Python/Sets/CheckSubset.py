T = int (input())
for i in range(T):
    A = int(input())
    a = set(map(int, input().split()))
    B = int(input())
    b = set(map(int, input().split()))
    if(a.issubset(b)):
        print("True")
    else:
        print("False")
