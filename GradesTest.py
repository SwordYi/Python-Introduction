from Grades import Grades
from MITPerson import *

def gradeReport(course):
    """假设course是Grades类型"""
    report = ''
    #for s in course.getStudents():
    for s in course.getStudentsByYield():
        tot = 0.0
        numGrades = 0        
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report = report + '\n' + str(s) \
                + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n' + str(s) \
                + ' has no grades'
    return report


ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)

for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)
sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)

print(gradeReport(sixHundred))