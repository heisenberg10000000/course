def only_one_positive(*args) -> bool:
    count_positive = 0
    for i in args:
        if i > 0:
            count_positive += 1
    return True if count_positive == 1 else False
