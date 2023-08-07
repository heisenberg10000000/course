a=[]
maximum=0
n,m=map(int,input().split())
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if a[i][j]>maximum:
            maximum=a[i][j]
            r=i
            c=j
        elif a[i][j]==maximum:
            if sum(a[r])<sum(a[i]):
                maximum=a[i][j]
                r=i
                c=j
print(r)
