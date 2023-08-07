def sum_num(a):
    s=0
    for i in a:
        if i.isdigit():
            s=s+int(i)
    print (s)
