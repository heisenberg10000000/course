a, b = map(int,input().split())
z=0 #сколько лет
while a<=b:
    z+=1
    a=a*3
    b=b*2
    
print(z) 
