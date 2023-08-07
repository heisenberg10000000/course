a = [] 
count = 0 
n, m = map(int, input().split())
for i in range(n):
    b = [] 
    for j in range(m):
        if i % 2 == 0:  
            b.append(count)
        if i % 2 == 1: 
            b.append(count)
            if j == (m - 1): 
                b.reverse()
        count += 1 
    a.append(b)  
for i in a:
    print(*i)  
