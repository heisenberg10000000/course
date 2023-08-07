x = int(input())
x1 = x
while x1 > 2:
    x1 -= 1
    if x % x1 == 0:
        print('No')
        break
else:
    if x == 1:
        print('No')
    else:
        print('Yes')
