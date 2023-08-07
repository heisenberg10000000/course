a=float(input())
b=float(input())
c=input()
if c == '/' and b != 0:
 print(a / b)
elif c == '/' and b == 0:
   print('Неизвестно')
elif c == '/' and a == 0:
   print('Неизвестно')
elif c == '*':
   print(a*b)
elif c == '+':
   print(a+b)
elif c == '-':
   print(a-b)
else:
   print('Неизвестно')
