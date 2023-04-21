n, r, t = map(int,input().split())
print(n ** 2 + r ** 2 == t**2 or r ** 2 + t ** 2 == n**2 or n ** 2 + t ** 2 == r**2)
