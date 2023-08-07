def create_dict():
    counter = 1
    history = dict()

    def append_hist(hist_val):
        nonlocal counter        
        history[counter] = hist_val
        counter += 1
        return history
    return append_hist
c1 = create_dict()
