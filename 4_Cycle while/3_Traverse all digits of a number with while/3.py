n=int(input())
result = 1
while n > 0:
    result *= n % 10
    n = n // 10
    
print (result)

