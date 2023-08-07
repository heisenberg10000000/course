n = int(input())
r = int(input())
t = int(input())
if n == r == t:
  print(3)
elif n == r or r == t or n == t:
  print(2)
else:
  print(0)
