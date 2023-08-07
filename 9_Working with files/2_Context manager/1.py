def find_lines_len_more_6(file_name):
    with open(file_name, 'r') as f:
        x = [str(i) for i in f.read().splitlines()]
        a = 0
        for i in x:
            if len(i) > 6:
                a +=1
        return a
