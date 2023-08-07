nums = int(input())
num_list = list(map(int, input().split()))
for i in range(len(num_list)-1):
    for j in range(len(num_list)-1):
        if num_list[j] > num_list[j+1]:
            num_list[j+1],num_list[j] = num_list[j],num_list[j+1]
print(*num_list)
