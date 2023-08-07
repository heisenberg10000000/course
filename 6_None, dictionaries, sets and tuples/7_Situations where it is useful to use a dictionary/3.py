s1 = input()
s2 = input()
d1 = {s: s1.count(s) for s in s1}
d2 = {s: s2.count(s) for s in s2}
print('YES' if d1==d2 and len(d1) == len(d2) else 'NO')
