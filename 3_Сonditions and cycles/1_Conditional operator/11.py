n = int(input())
d6 = n%10
d5 = n//10%10
d4 = n//100%10
d3 = n//1000%10
d2 = n//10000%10
d1 = n//100000
if d6+d5+d4==d1+d2+d3:
  print('YES')
else:
  print('NO')
