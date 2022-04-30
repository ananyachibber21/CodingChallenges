# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    S = input()
    s1 = ""
    s2 = ""
    
    for j in range(len(S)):
        if(j%2==0):
            s1 = s1 + S[j]
        else:
            s2 = s2 + S[j]
    print(s1+" "+s2)       
        
