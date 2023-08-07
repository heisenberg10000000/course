def create_actor(**kwargs):
    f = {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46
    }

    return f | kwargs

