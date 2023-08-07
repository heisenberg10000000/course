sum = 0
for i in range(1000, 10000):
    if sum(map(int, str(i))) == 20:
        sum += i
print(sum)
