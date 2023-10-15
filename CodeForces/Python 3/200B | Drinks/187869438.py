def solve():
    
    n=int(input())
    p=map(int,input().split(' '))
    res=0
    for x in p:
        res+=x/n
    print(res)
    
    
        
            
        
    return
            
    
t=1
for _ in range(t):
    solve()