a = input().split()
m = []
for i in a:
    if i.lower() not in [e.lower() for e in m]:
        m.append(i)
print(" ".join(m))
