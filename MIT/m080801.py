# -*- coding:utf-8 -*-
from m080301 import *


class GradesYield(Grades):

    def getStudents(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s


if __name__ == "__main__":

    book = GradesYield()
    book.addStudent(Grad('Julie '))
    book.addStudent(Grad('Charlie '))
    for s in book.getStudents():
        print(s)