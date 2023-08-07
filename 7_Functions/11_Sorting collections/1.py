subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93),('History', 82)]

c = sorted(subject_marks, key=lambda x: int(x[1]), reverse=False)  
for i in c:   
    print(*i)
