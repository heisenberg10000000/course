n = int(input())

i = 1
a = []

while i<=n:
    if n % i == 0:
        a.append(i)
    i += 1
    
print(a[1])
