if __name__ == "__main__":
    A = int(input())
    a = set(map(int, input().split()))
    N = int(input())
    for i in range(N):
        x, *y = input().split()[0], set(map(int, input().split()))
        getattr(a,x)(*y)
    print(sum(a))
