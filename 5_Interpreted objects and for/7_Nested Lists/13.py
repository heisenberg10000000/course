matrix = []

for i in range(4):
    matrix.append(input())


for i in range(4):
    for j in range(4):
        if j != 3 and matrix[i][j] == matrix[i][j+1]:
            if i != 3 and j != 3 and matrix[i+1][j] == matrix[i+1][j+1] and matrix[i+1][j+1] == matrix[i][j]:
                print("No")
                exit()
print("Yes")
