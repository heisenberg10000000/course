a,b=map(int,input().split())
s=[]
q=[]
for i in range(a):
    s.append(list(map(int,input().split())))
for i in range(a):
        q.append(sum(s[i]))
print(max(q))
print(q.index(max(q)))
