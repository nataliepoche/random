class Student:
    def __init__(self, name, gpa):
        self._name = name
        self._gpa = gpa

    def __it__(self, other):
        return self._name < other._name  # "_" protected and in accessible from outside class

    def get_gpa(self):
        return self._gpa

    def get_name(self):
        return self._name


class Course:
    def __init__(self):
        self.roster = []  # list of Student objects

    def add_student(self, student):
        self.roster.append(student)

    def search_student(self, target_name):
        self.roster.sort()
        start = 0
        end = len(self.roster) - 1
        while start <= end:
            middle = (start + end) // 2
            if self.roster[middle]._name == target_name:
                return True
            elif self.roster[middle]._name < target_name:
                start = middle + 1
            else:
                end = middle - 1
        for student in self.roster:
            if student.get_name() == target_name:
                return True
            else:
                return False
        return False


if __name__ == "__main__":
    course = Course()

    course.add_student(Student('Henry Nguyen', 3.5))
    course.add_student(Student('Brenda Stern', 2.0))
    course.add_student(Student('Lynda Robinson', 3.2))
    course.add_student(Student('Sonya King', 3.9))

    print(course.search_student('Amanpreet Kapoor'))
    print(course.search_student('Lynda Robinson'))
