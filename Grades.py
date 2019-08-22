from MITPerson import *

class Grades(object):
    def __init__(self):
        """ 创建一个空的成绩册 """
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """ 假设student为Student类型，将student添加到成绩册 """
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """ 假设grade为浮点数，将grade添加到student的成绩列表 """
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def getGrades(self, student):
        """ 返回student的成绩列表 """
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def getStudents(self):
        """ 返回成绩册中排号序的成绩列表 """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

    def getStudentsByYield(self):
        """ 按字母顺序返回成绩册中排号序的成绩列表，
            使用生成器方式 """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s