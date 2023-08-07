str, stb = map(int, input().split()) 
a = []
b = []
c = []
for i in range(str):
    a.append(list(map(int, input().split())))
for i in range(str):
    s = 0
    for j in range(stb):
        s = s + a[i][j]
    b.append(s)
for j in range(stb):
    s1 = 0
    for i in range(str):
        s1 = s1 + a[i][j]
    c.append(s1)
print(*b)
print(*c)
