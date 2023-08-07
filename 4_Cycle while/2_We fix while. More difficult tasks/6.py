n, m = (int, input().split()) 
list1 = list(map(int, input().split())) 
list2 = list(map(int, input().split())) 
list = list1 + list2  

result = []  


while len(list) != 0:
    a = min(list)    
    result.append(a)  
    list.remove(a)    

print(*result)

