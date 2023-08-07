mas = []
for i in range(5):
    mas.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if mas[i][j] == 1:
            row = i
            column = j
            
print(abs(2 - row) + abs(2 - column))
