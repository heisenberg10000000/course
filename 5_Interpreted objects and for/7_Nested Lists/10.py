n, m = map(int, input().split())
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    
maximum = 0
i_max = 0
j_max = 0
for i in range(n):
    for j in range(m):
        if a[i][j] > maximum:
            maximum = a[i][j]
            i_max = i
            j_max = j

print(maximum)
print(i_max, j_max)
