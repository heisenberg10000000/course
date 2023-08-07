n, m = map(int, input().split())    
photo = [input().split() for _ in range(n)]

colors = ['C', 'M', 'Y']   
flagColor = '#Black&White'      

for i in range(n):               
    for j in range(m):          
        if photo[i][j] in colors:
            flagColor ='#Color' 
            
print(flagColor)
