a, b = map(int, input().split())  
a1, b1 = a, b                     

while b > 0:
    a, b = b, a % b                    
print(a1 * b1 // a)

