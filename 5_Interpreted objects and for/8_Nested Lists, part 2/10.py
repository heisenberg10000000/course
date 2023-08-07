r, c = map(int, input().split())

tort = []
for i in range(r):
    tort.append(input())

mas = [[False]*c for i in range(r)]
for i in range(r):
    if 'S' not in tort[i]:
        for j in range(c):
            mas[i][j] = True
for j in range(c):
    is_find = False
    for i in range(r):
        if tort[i][j] == 'S':
            is_find = True
            break
    if not is_find:
        for i in range(r):
            mas[i][j] = True
count = 1
for row in mas:
    count += row.count(True)
print(count-1)
