def text_decor(func):
    def dec(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')
    return dec
