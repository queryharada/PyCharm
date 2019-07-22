# -*- coding:utf-8 -*-
from m080103 import *


class Grades(object):

    def __init__(self):
        self.students = list()
        self.grades = dict()
        self.isSorted = True

    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student ')
        self.students.append(student)
        self.grades[student.getIdNum()] = list()
        self.isSorted = False

    def addGrade(self, student, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping ')

    def getGrades(self, student):
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping ')

    def getStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]


def gradeReport(course):
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report = report + '\n' \
                     + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n' \
                     + str(s) + ' has no grades '
    return report


if __name__ == "__main__":

    ug1 = UG('Jane Doe', 2014)
    ug2 = UG('Jane Doe', 2015)
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
