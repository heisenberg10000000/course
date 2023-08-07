a = input()
s = 0
ss = 0
for i in a:
    if i.isdigit():
        i = int(i)
        ss += int(i)
        s += 1
print(s,ss)
