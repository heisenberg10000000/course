def find_keys (**kwargs):
    res = [k for k,v in kwargs.items() if isinstance(v, (list, tuple))]
    return (sorted(res, key=str.lower))
