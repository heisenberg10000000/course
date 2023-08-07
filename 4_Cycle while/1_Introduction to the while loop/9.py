time = 0
a, b = map(int, input().split())
while a > 0:
    a -= 1
    time += 1
    if time % b == 0:
        a += 1
print(time)

