a = int(input())
p = 0
for i in range(a + 1, 2 * a):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        p += 1
print(p)
