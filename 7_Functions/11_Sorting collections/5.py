products = []


while True:
    input_str = input().strip()
    if input_str == 'конец':
        break
    name, price = input_str.split(': ')
    price = int(price)
    products.append((name, price))


products.sort(key=lambda x: x[1], reverse=True)


for product in products:
    print(product[0])
