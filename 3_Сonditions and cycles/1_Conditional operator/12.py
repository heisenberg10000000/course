s = '_abcdefgh'
coord_1 = input()
coord_2 = input()
letter_1 = coord_1[0]
letter_2 = coord_2[0]
column_1 = s.find(letter_1)
column_2 = s.find(letter_2)
row_1 = int(coord_1[1])
row_2 = int(coord_2[1])
if (row_1 + column_1) % 2 == (row_2 + column_2) % 2:
  print('YES')
else:
  print('NO')
