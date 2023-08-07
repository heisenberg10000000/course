def my_range_gen(*args):
   if len(args) == 1:
       start = 0
       stop = args[0]
       step = 1
   elif len(args) == 2:
       start = args[0]
       stop = args[1]
       step = 1
   elif len(args) == 3:
       start = args[0]
       stop = args[1]
       step = args[2]
   else:
       raise TypeError('my_range_gen expects 1-3 arguments, got ' + str(len(args)))

   if step == 0:
       return

   if (step > 0 and start >= stop) or (step < 0 and start <= stop):
       return

   i = start
   while (step > 0 and i < stop) or (step < 0 and i > stop):
       yield i
       i += step
