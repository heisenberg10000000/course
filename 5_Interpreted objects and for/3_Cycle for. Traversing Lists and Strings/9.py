n = input()
s_even = 0
s_odd = 0
for i in range(len(n)):
    if i % 2 == 0:
        s_even += int(n[i])
    else:
         s_odd += int(n[i])
diff = s_even - s_odd
if diff % 11 == 0:
    print("YES")
else:
    print("NO")

