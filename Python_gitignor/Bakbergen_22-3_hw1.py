class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Name: {self.fullname} Age: {self.age} Is married: {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        return sum(self.marks.values()) / len(self.marks)


class Teacher(Person):
    salary = 15000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def count_extra_salary(self):
        return self.salary + (int(self.salary / 100 * 5) * (self.experience - 3) if self.experience > 2 else 0)


Esen = Teacher('Esen Back', 19, False, 4)
Esen.introduce_myself()
print(Esen.count_extra_salary())


def create_students():
    students = []
    students.append(Student('Asylbek', 17, False, {'math': 5, 'geography': 4}))
    students.append(Student('Bakbergen', 18, False, {'history': 4, 'Fizra': 5}))
    students.append(Student('Almaz', 17, False, {'everything': 2}))
    return students

students = create_students()
for student in students:
    student.introduce_myself()
    for subject, mark in student.marks.items():
        print(subject, mark)
    print(student.average_mark())
