class Student:
    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade

    def get_grade(self):
        return self._grade


class Course:
    def __init__(self, name, max_number):
        self._name = name
        self._max_number = max_number
        self.students = []

    def add_student(self, student):
        if len(self.students) < self._max_number:
            self.students.append(student)
            return True
        return False

    def get_student_average(self):
        value = 0
        for i in self.students:
            value += i.get_grade()
        return value/len(self.students)


s1 = Student('Dayo', 1, 100)
s2 = Student('Tosin', 35, 99)

c = Course('Python', 3)
c.add_student(s1)
c.add_student(s2)

print(c.get_student_average())
