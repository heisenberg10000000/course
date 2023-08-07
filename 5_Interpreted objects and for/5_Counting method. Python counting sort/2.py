n = int(input())
a = input().split(' ')
s = [0] * 201
for i in a:
    s[int(i) + 100] += 1
for i in range(len(s)):
    if s[i] > 0:
        print((str(i - 100) + ' ') * s[i], end='')
