names = ['Дили', 'Вили', 'Били']
d = {name: set() for name in names}
for s in iter(input, 'конец'):
   name, comment = s.split(': ')
   d[name].add(comment)
d = {k: len(v) for k, v in d.items()}
for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
   print(f'Количество уникальных комментаторов у {k} - {v}')
