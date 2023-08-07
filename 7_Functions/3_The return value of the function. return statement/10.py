def factorial(n):
    if n == 0:
        return 0
    if n == 1:
        return n
    else:
        return n * int(factorial(n - 1))


def trailing_zeros(n):
    if n == 0:
        return 0
    count = 0
    for i in list(str(factorial(n))[::-1]):
        if i == '0':
            count += 1
        else:
            return count

# код ниже не стоит удалять, он нужен для проверки
assert trailing_zeros(0) == 0
assert trailing_zeros(6) == 1
assert trailing_zeros(30) == 7
assert trailing_zeros(12) == 2      
print('Проверки пройдены')
