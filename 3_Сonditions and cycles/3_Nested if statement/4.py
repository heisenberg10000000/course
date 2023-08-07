a, b, c = map(int, input().split())

if a > b:
    if b > c:
        print(a - c)
    else:
        if c > a:
            print(c-b)
        else:
            print(a-b)
else:
    if b > a:
        if a > c:
            print(b - c)
        else:
            if c > b:
                print(c-a)
            else:
                print(b-a)
 
