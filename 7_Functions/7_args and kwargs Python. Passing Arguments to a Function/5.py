def print_goods(*args):
    c = 1
    for i in args:
        if type(i) == str and len(i) > 0:
            print(f'{c}. {i}')
            c += 1
    if c == 1:
        print('Нет товаров')
