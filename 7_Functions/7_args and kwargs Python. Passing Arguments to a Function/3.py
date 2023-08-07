def multiply(*args):
    pr = 1
    if args:
        for i in args:
            pr *= i
        return(pr)
    else:
        return(pr)

