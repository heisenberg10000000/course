a = input()
b = input()
if len(a) < 7:
  print("Short")
elif len(a) == len(b):
  print("OK")
elif len(a) != len(b):
  print("Difference")
