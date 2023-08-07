n = int(input()) 
bdays = {} 
for i in range(n):
   name, day, month = input().split()
   bdays.setdefault(month, []).append(name) 
m = int(input()) 
for i in range(m):
   month = input().strip()
   if month in bdays:
       names = sorted(bdays[month]) 
       print(' '.join(names))
   else:
       print('Нет данных')

