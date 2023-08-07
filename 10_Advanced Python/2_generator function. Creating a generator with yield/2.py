def gen_fibonacci_numbers(n):

    a, b = 1, 1

    for i in range(n):

        yield a

        a, b = b, a + b

