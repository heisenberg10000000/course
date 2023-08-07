n = int(input())
my_dict = {}
for i in range(1, n+1):
    my_dict.setdefault(i, i**2)
print(my_dict)
