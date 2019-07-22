# -*- coding:utf-8 -*-
import datetime


class Person(object):

    def __init__(self, name):
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name
        self.birthday = None

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def setBirthday(self, birthdate):
        self.birthday = birthdate

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name


class MITPerson(Person):
    nextIdNum = 0

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        return self.idNum < other.idNum

    def isStudent(self):
        return isinstance(self, Student)


class Student(MITPerson):
    pass


class UG(Student):  # Undergraduate
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year


class Grad(Student):
    pass

class TransferStudent(Student):  # Undergraduate
    def __init__(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool

    def getOldSchool(self):
        return self.fromSchool

if __name__ == "__main__":

    me = Person('Michael Guttag')
    him = Person('Barack Hussein Obama')
    her = Person('Madonna')
    print(him.getLastName())
    him.setBirthday(datetime.date(1961, 8, 4))
    her.setBirthday(datetime.date(1958, 8, 16))
    print(him.getName(), 'is', him.getAge(), 'days old')

    pList = [me, him, her]
    for p in pList:
        print(p)
    pList.sort()
    for p in pList:
        print(p)
    print('###################################')

    p1 = MITPerson('Barbara Beaver')
    print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
    print('###################################')

    p1 = MITPerson('Michael Guttag ')
    p2 = MITPerson('Billy Bob Beaver ')
    p3 = MITPerson('Billy Bob Beaver ')
    p4 = Person('Billy Bob Beaver ')

    print('p1 < p2', p1 < p2)
    print('p3 < p2', p3 < p2)
    print('p4 < p1', p4 < p1)
    # print('p1 < p4', p1 < p4)  # p4 は idNumがない
    print('###################################')

    p5 = Grad('Buzz Aldrin ')
    p6 = UG('Billy Beaver ', 1984)
    print(p5, 'is a graduate student is ', type(p5) == Grad)
    print(p5, 'is an ungraduate student is ', type(p5) == UG)
    print('###################################')

    print(p5, 'is a student is', p5.isStudent())
    print(p6, 'is a student is', p6.isStudent())
    print(p3, 'is a student is', p3.isStudent())
    print('###################################')



