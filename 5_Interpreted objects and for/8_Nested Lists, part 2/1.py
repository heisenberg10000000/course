n = int(input())
maks = 0
for i in range(n):
    a = list(map(int,input().split()))
    if maks < a[-(i+1)]:
        maks = a[-(i+1)]
print(maks)
