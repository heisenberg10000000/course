a = input()                 
b = list(input().split())
g = len(b)                

for i in range(g):               
    if a in b[i].lower():    
        print(b[i])
