n, m = map(int, input().split())
start = []

for i in range(n):
    start.append(input())
input()
finish =[]

for i in range(n):
    finish.append(input())
count = 0
for row in range(n):
    for col in range(m):
        if start[row][col] == finish[row][col]:
            count += 1
print(count)
