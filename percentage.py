#WAP to input name, class, section, marks of 5 subjects, total marks, grade, percntage. print in proper manner
n = input("Enter your name: ")
c = input("Enter your class: ")
s = input("Enter your section: ")
s1 = float(input("Enter marks obtained in English: "))
s2 = float(input("Enter marks obtained in Hindi: "))
s3 = float(input("Enter marks obtained in Maths: "))
s4 = float(input("Enter marks obtained in Science: "))
s5 = float(input("Enter marks obtained in Social Science: "))
tmm = int(input("Enter maximum marks obtainable in a subject: "))
tmm1 = tmm*5
tmmo = s1 + s2 + s3 + s4 + s5
p = round(tmmo*100/tmm1,2)
if p >= 90:
    g = "Passed with A1 grade"
elif p >= 80:
    g = "Passed with A2 grade"
elif p >= 70:
    g = "Passed with B1 grade"
elif p >= 60:
    g = "Passed with B2 grade"
elif p >= 50:
    g = "Passed with C1 grade"
elif p >= 40:
    g = "Passed with C2 grade"
elif p >= 30:
    g = "Passed with D grade"
else:
    g = "Failed"
print('''Name: {0}
Class: {1}
Section: {2}
Total Marks Obtained = {3}
Percentage(%): {4}
Result: {5}'''.format(n,c,s,tmmo,p,g))
'''
Output:
Enter your name: Pulkit
Enter your class: XI
Enter your section: C
Enter marks obtained in English: 96
Enter marks obtained in Hindi: 95
Enter marks obtained in Maths: 100
Enter marks obtained in Science: 99
Enter marks obtained in Social Science: 98
Enter maximum marks obtainable in a subject: 100
Name: Pulkit
Class: XI
Section: C
Total Marks Obtained = 488.0
Percentage(%): 97.6
Result: Passed with A1 grade
'''