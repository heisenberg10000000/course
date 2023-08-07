a = input().lower().strip('ьъы')[-1] 
b = input().lower()[0]
if a == b:
  print("Good")
else:
  print("Bad")
