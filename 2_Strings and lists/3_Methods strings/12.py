n = input().lower()
n = n.replace('o', '')
n = n.replace('a', '')
n = n.replace('y', '')
n = n.replace('e', '')
n = n.replace('u', '')
n = n.replace('i', '')
n = '.'.join(n)
print('.' + n)
