def double_fact(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    f = n * double_fact(n-2)
    return f
