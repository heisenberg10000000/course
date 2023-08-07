n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
    
maximum = 0
count = 0
for i in range(n):
    local_maximum = 0
    for j in range(m):
        if a[i][j] >  local_maximum:
            local_maximum = a[i][j]
    if local_maximum > maximum:
        maximum = local_maximum
        count = 1
    elif local_maximum == maximum:
        count += 1
print(count)
