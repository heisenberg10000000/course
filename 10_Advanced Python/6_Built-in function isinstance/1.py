def count_strings(*args):
    k=list(filter(lambda arg:type(arg)==str,args))
    return len(k)

