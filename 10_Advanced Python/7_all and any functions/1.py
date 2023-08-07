z, x = [], input().split()
for i in range(len(x)):
    z.append('A' in x[i])
print(any(z))
