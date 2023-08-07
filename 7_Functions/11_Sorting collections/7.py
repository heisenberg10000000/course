d={}                       
for i in range(int(input())):
    a=input().split()      
    if a[1] not in d:       
        d[a[1]]=[a[0]]
    elif a[1] in d:         
        d[a[1]].append(a[0])
for i in range(int(input())):
    b=input()              
    if b in d:             
        print(*d[b])
    else:                
        print('Неизвестный номер')
