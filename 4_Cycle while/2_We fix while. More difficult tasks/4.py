a, b = map(int, input().split()) 
c = 0  
d = 240 - b
while d > 0:
    c+=1
    d-=c*5
    if a == c: 
        break

if d<0:
    c-=1
print(c)
