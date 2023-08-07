n = int(input())
hour = (n // 3600) % 24
n = n % 3600
minutes =  n // 60
n = n % 60
sec = n
print(hour, ':', minutes // 10, minutes %10, ':', sec // 10, sec % 10, sep='')
