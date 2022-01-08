if __name__ == '__main__':
    d={}
    for i in range(int(input())):
        name = input()
        score = float(input())
        d[name]=score
    v = d.values()
    sort = sorted(list(set(v)))
    val = sort[1]
    l=[]
    for key,value in d.items():
        if(value==val):
            l.append(key)
    l.sort()
    for j in l:
        print(j)
