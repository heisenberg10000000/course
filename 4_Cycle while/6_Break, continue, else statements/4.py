s = input()
l = list(s)
while len(l) > 0:
    if l[0] == 'e' or l[0] == 'a':
        print("Ага! Нашлась")
        break
    print(f"Текущая буква: {l[0]}")
    del l[0]
else:
    print("Распечатали все буквы")
