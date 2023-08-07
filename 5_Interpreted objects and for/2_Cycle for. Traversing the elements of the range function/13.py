n = int(input())
for i in range(n):
    a = input()
    if len(a) < 10:
        print(a)
    else:
        m = a[0]+str(len(a[1:-1]))+a[-1]
        print(m)
