def outer() -> None:
    def say_hello() -> None:
        h = 'hello'
        print(h)

    def say_bye() -> None:
        b = 'bye'
        print(b)


    say_bye()
    say_hello()

outer()
