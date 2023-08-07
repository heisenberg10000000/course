n = int(input())
i = 0
while 2**i < n:
   i += 1
if 2**i == n:
   print(i)
else:
   print('НЕТ')
