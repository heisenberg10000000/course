n=int(input())
f=int(input())
s,q=0,0
for i in range(n,f+1):
    s,q=i**2,i**3
    res="Число {i}; его квадрат = {s}; его куб = {q}".format(i=i,s=s,q=q)
    print(res)
