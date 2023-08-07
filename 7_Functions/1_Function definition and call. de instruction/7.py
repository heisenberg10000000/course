def check_password(password):
    count_digit = 0
    count_upper = 0
    count_spec = 0
    for s in password:
        if s.isdigit(): 
            count_digit += 1

        if s.isupper():
            count_upper  += 1

        if s in "!@#$%*":
            count_spec  += 1
            
    if count_digit >= 3 and count_upper > 0 and count_spec > 0 and len(password) >= 10:
        print('Perfect password')
    else:
        print('Easy peasy')
        
