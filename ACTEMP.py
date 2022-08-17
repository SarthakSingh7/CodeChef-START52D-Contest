for i in range(int(input())):
    t = input().split()
    a = int(t[0])  # at least
    b = int(t[1])  # at most
    c = int(t[2])  # at least
    l = []
    lm = max(a,b,c)
    for i in range(0,lm + 1):
        l.append(i)
    flag = 0    
    for i in l:
        if i >= a and i<= b and i >= c:
            flag = 1
    if flag:
        print('Yes')
    else:
        print('No')
        
    
