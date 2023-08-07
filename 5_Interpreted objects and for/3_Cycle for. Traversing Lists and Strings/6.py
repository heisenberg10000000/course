a = input().split()
r = input()

n = len(a)
for i in range(n):
    if a[i] == r:
        print(i + 1)
        break
else:       
        print("ErrorValue")


