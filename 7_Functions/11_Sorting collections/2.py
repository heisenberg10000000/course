subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]

c = sorted(subject_marks, key=lambda x: int(x[1]), reverse=True)  
for i in c:    
    print(*i)
