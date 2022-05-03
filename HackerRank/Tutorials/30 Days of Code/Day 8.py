# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
dict = {}
for i in range(n):
    item = input().split()    
    dict[item[0]] = item[1]
while True:
    try:
       name = input()
       if(name in dict.keys()):
         print(name+ "="+ dict[name])
       else:
         print("Not found") 
    except EOFError:
        break


