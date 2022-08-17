for i in range(int(input())):
    n = int(input())
    s = input().split()
    v = input()
    WA = []  # contains the index of WA cases
    WA_case = []
    for i in range(n):
        if v[i] == '0':
            WA.append(i)
    for i in WA:
        WA_case.append(int(s[i]))
    print(min(WA_case))    
        
        
            
