def calculate(x:float, y:float, operation:str='a') -> None:
    def addition():     
        print(x + y)
        
    def subtraction():  
        print(x - y)
        
    def division():      
        print('На ноль делить нельзя!' if y == 0 else x / y)
        
    def multiplication(): 
        print(x * y)
        
    if operation == 'a':  
        addition()
    elif operation == 's': 
        subtraction()
    elif operation == 'd': 
        division()
    elif operation == 'm':
        multiplication()
    else:                
        
        print('Ошибка. Данной операции не существует')

