sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}
sweet.setdefault('weight',230)
sweet.setdefault('have_topping',True)
sweet['name']='SuperCake'
sweet['calories'] = 350
print(sweet)
