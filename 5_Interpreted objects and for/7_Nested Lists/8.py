n = int(input())
mas = []
for i in range(n):
    mas.append(list(map(int, input().split())))
     
count = 0        
for i in range(n):
    for j in range(n):
        if mas[i][j] != mas[j][i]:
           count += 1
if count > 0:     
   print('No')
else:
   print('Yes')
    
