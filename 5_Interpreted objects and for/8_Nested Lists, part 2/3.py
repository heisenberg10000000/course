n = int(input())
commands = []
for i in range(n):
    home, guest = map(int, input().split())
    commands.append([ home, guest])

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if commands[i][0] == commands[j][1]:
            count += 1
        if commands[i][1] == commands[j][0]:
            count += 1

print(count)
