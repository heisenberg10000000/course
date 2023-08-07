a = {}               
n = int(input())      
for i in range(n):   
    string = input()  
    if string not in a: 
        a[string] = 1
    else:            
        a[string] += 1
minimum = min(a.items(), key=lambda x: x[1])  
maximum = max(a.items(), key=lambda x: x[1]) 
if len(a) >= 1:      
    print(*maximum, sep=', ')
    print(*minimum, sep=', ')

