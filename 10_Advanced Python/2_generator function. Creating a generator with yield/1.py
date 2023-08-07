def gen_squares(n):
    b=(i**2 for i in range(1,n+1))
    for i in b:
       yield i
