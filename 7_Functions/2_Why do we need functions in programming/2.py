# объявление функции
def is_between(name, surname, middlename):
# если первый аргумент находиться между вторым и третьим(включительно), то выводим True
    if surname <= name <= middlename or surname >= name >= middlename:  
        print(True)
    else:              # иначе False
        print(False)
# считываем данные
a, b, c = map(int, input().split())
# вызываем функцию
is_between(a, b, c)
