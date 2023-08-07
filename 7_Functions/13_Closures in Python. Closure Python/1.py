def create_accumulator():
    total = 0 
    def accumulator(number): 
        nonlocal total 
        total += number 
        return total 
    return accumulator
