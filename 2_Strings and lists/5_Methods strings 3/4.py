
a = int(input())
b = int(input())
c = int(input())

a = hex(a)[2:].zfill(2).upper()
b = hex(b)[2:].zfill(2).upper()
c = hex(c)[2:].zfill(2).upper()

print('#'+a+b+c)
