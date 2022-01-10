if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        command, *val = input().split()
        arg = list(map(int, val)) 
        if(command == "insert"):
            l.insert(arg[0], arg[1])
        elif(command == "remove"):
            l.remove(arg[0])
        elif(command == "append"):
            l.append(arg[0])
        elif(command == "sort"):
            l.sort()
        elif(command == "pop"):
            l.pop()
        elif(command == "reverse"):
            l.reverse()
        elif(command == "print"):
            print(l)       
