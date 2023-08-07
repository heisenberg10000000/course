n = int(input())
for i in range(n):
    s = input().lower()
    if "рок" in s:
        print(i + 1, s.find('рок') + 1)

