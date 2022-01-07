if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    sets = set(arr)
    sort = sorted(sets)
    print(sort[-2])
