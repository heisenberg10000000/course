n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    
for column in range(n-1, -1, -1):
    for row in range(n-1, -1, -1):
        print(a[row][column], end = ' ')
    print()
    
