#WAP to input name, class, section, marks of 5 subjects, total marks, grade, percntage. print in proper manner, use list func
l=[]
l.append(input("Enter your name: "))
l.append(input("Enter your class: "))
l.append(input("Enter your section: "))
l.append(float(input("Enter marks obtained in English: ")))
l.append(float(input("Enter marks obtained in Hindi: ")))
l.append(float(input("Enter marks obtained in Maths: ")))
l.append(float(input("Enter marks obtained in Science: ")))
l.append(float(input("Enter marks obtained in Social Science: ")))
l.append(float(input("Enter marks obtained in Sanskrit: ")))
tmm = int(input("Enter maximum marks obtainable in a subject: "))
tmm1 = tmm*6
l.append(l[3] + l[4] + l[5] + l[6] + l[7] + l[8])
l.append(round(l[9]*100/tmm1,2))
if l[10] >= 90:
    g = "Passed with A1 grade"
elif l[10] >= 80:
    g = "Passed with A2 grade"
elif l[10] >= 70:
    g = "Passed with B1 grade"
elif l[10] >= 60:
    g = "Passed with B2 grade"
elif l[10] >= 50:
    g = "Passed with C1 grade"
elif l[10] >= 40:
    g = "Passed with C2 grade"
elif l[10] >= 30:
    g = "Passed with D grade"
else:
    g = "Failed"
l.append(g)
print('''
Name of the student: {}
Class: {}-{}
Marks obtained in English: {}
Marks obtained in Hindi: {}
Marks obtained in Maths: {}
Marks obtained in Science: {}
Marks obtained in Social Science: {}
Marks obtained in Sanskrit: {}
Total marks obtained: {}
Percentage obtained(%): {}
Result: {}'''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9],l[10],l[11]))

'''
output:
Name of the student: Saumya Sukhija
Class: VIII-D
Marks obtained in English: 46.0
Marks obtained in Hindi: 53.0
Marks obtained in Maths: 53.0
Marks obtained in Science: 47.0
Marks obtained in Social Science: 51.0
Marks obtained in Sanskrit: 57.0
Total marks obtained: 307.0
Percentage obtained(%): 85.28
Result: Passed with A2 grade
'''