def solve():
    
    n=int(input())
    res=0
    for _ in range(n):
        s=input().split(' ')
        c=0
        for x in s:
            if x=='1':
                c+=1
        if c>=2:
            res+=1
    print(res)
        
            
        
    return
            
    
t=1
for _ in range(t):
    solve()