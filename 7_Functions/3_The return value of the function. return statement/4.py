def generate_fizz_buzz_list(n):
    c =[]  
    for i in range(1, n+1):
           
        if i % 3 == 0 and i % 5 == 0:
            c.append('FizzBuzz')
                  
        elif i % 3 == 0:
            c.append('Fizz')
        elif i % 5 == 0:
            c.append('Buzz')
        else:
            c.append(i)
    return c

