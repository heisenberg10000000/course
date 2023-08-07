def rev(n):                        
    if n > 0:                          
        rev(n-1)                      
        print(sp[-n], end=" ")   

N = int(input())                           
sp = list(map(int, input().split())) 
rev(N)  
