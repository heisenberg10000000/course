def create_accumulator(optional=0):
    def inner(value):
        nonlocal optional
        optional += value
        return optional

    return inner

