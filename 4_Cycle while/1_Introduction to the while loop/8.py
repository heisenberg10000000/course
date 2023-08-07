socks, mama = map(int, input().split())
day = 0
while socks > 0:
  socks -= 1
  day += 1
  if day % mama == 0:
   socks += 1
print(day)
