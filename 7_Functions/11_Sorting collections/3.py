subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
a = sorted(subject_marks)                  
b = sorted(a, key=lambda x: x[1], reverse=True)
for i in b:                                  
    print(*i)

