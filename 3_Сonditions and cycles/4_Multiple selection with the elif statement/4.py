age = int(input())
if age < 2:
  print("Маденец")
elif age >= 2 and age < 3:
  print("Малыш")
elif age >= 4 and age < 11:
  print("Ребенок")
elif age >= 12 and age < 18:
  print("Подросток")
elif age >= 19 and age < 64:
  print("Взрослый человек")
elif age >= 65:
  print("Пожилой человек")
