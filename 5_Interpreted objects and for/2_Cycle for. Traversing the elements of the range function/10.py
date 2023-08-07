n = int(input())
B = 0
C = 0

for i in range(n):
    b, c = map(int, input().split())
    if b > c:
        B += 1
    elif b < c:
        C += 1
        
if B > C:
    print("Mishka")
elif B < C:
    print("Chris")
elif B == C:
    print("Friendship is magic!^^")
