class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def AverageGrade(self):
        sum_grades = 0
        count_grades = 0
        for course, grades in self.grades.items():
            sum_grades += sum(grades)
            count_grades += len(grades)
        AvGr = sum_grades/count_grades
        return AvGr
    
    def __str__(self):
        AvGrtoStr = self.AverageGrade()
        res = f'\n Имя: {self.name}\n Фамиля:  {self.surname}\n Средняя оценка за домашние задания:  {AvGrtoStr:0.1f}\n Курсы в процессе изучения:{", ".join(self.courses_in_progress)} \n Завершенные курсы: {", ".join(self.finished_courses)}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.AverageGrade() < other.AverageGrade()
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer (Mentor):
    def __init__(self,name,surname):
         super().__init__(name, surname)
         self.grades = {}

    def AverageGrade(self):
        sum_grades = 0
        count_grades = 0
        for course, grades in self.grades.items():
            sum_grades += sum(grades)
            count_grades += len(grades)
        AvGr = sum_grades/count_grades
        return AvGr
    
    def __str__(self):
        AvGrtoStr = self.AverageGrade()
        res = f'\nИмя: {self.name}\n Фамиля:  {self.surname}\n Средняя оценка за лекции:  {AvGrtoStr:0.1f}'
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.AverageGrade() < other.AverageGrade()

class Reviewer (Mentor):
    def __str__(self):
         res = f'\nИмя: {self.name}\nФамиля = {self.surname}'
         return res
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
def AverageGradeCourseSt(all_student, course):
    sum_grades = 0
    count_grades = 0
    for student in all_student:
        for course_student, grades_students in student.grades.items():
            if course_student == course:
                sum_grades += sum(grades_students)
                count_grades += len(grades_students)
    res = sum_grades/count_grades
    return(res)

def AverageGradeCourseLt(all_lecturer, course):
    sum_grades = 0
    count_grades = 0
    for lecturer in all_lecturer:
        for course_lecturer, grades_lecturer in lecturer.grades.items():
            if course_lecturer == course:
                sum_grades += sum(grades_lecturer)
                count_grades += len(grades_lecturer)
    res = sum_grades/count_grades
    return(res)

all_student = []
Anna_student = Student('Anna', 'Russkih', 'woman')
Anna_student.courses_in_progress += ['Python']
Anna_student.courses_in_progress += ['Git']
Anna_student.finished_courses += ['Java']
Anna_student.grades['Python'] = [10,9,8]
Anna_student.grades['Git'] = [10,9,10]
# print(Anna_student)
Anna_student.add_courses('JS')
all_student.append(Anna_student)
# print(Anna_student)

Kate_student = Student('Kate', 'Koroleva', 'woman')
Kate_student.courses_in_progress += ['Python']
Kate_student.courses_in_progress += ['Git']
Kate_student.finished_courses += ['JS']
Kate_student.grades['Python'] = [10,9,10]
Kate_student.grades['Git'] = [10,9,10,8]
# print(Kate_student)
all_student.append(Kate_student)

Ivan_Lecturer = Lecturer('Ivan', 'Ivanov')
Ivan_Lecturer.courses_attached += ['Python', 'JS']


Petr_Lecturer = Lecturer('Petr', 'Petrov')
Petr_Lecturer.courses_attached += ['Git', 'Python']

Anna_student.rate_l(Ivan_Lecturer, 'Python', 8)
Anna_student.rate_l(Petr_Lecturer, 'Git',9)

Kate_student.rate_l(Ivan_Lecturer, 'Python', 10)
Kate_student.rate_l(Petr_Lecturer, 'Git',8)
print('ЛЕКТОРЫ:')
print(Ivan_Lecturer)
print(Petr_Lecturer)

Tom_Reviewer = Reviewer('Tom', "Jobs")
Tom_Reviewer.courses_attached += ['Python']
Tom_Reviewer.rate_hw(Anna_student, 'Python',5)

Jon_Reviewer = Reviewer('Jon', "Jobs")
Jon_Reviewer.courses_attached += ['Git']
Jon_Reviewer.rate_hw(Kate_student, 'Git',5)

print('\nПРОВЕРЯЮЩИЕ:')
print(Tom_Reviewer)
print(Jon_Reviewer)

print('\nСТУДЕНТЫ:')
print(Anna_student)
print(Kate_student)

print('\nСравнение студентов:')
if Anna_student > Kate_student:
    print(f'Средняя оценка за ДЗ выше у {Anna_student.name} {Anna_student.surname}')
elif Anna_student < Kate_student:
    print(f'Средняя оценка за ДЗ выше у {Kate_student.name} {Kate_student.surname}')
else:
    print(f' Средние баллы за ДЗ {Anna_student.name} {Anna_student.surname} и {Kate_student.name} {Kate_student.surname} равны')

print('\nСравнение лекторов:')
if Ivan_Lecturer > Petr_Lecturer:
    print(f'Средняя оценка выше у {Ivan_Lecturer.name} {Ivan_Lecturer.surname}')
elif Ivan_Lecturer <  Petr_Lecturer:
    print(f'Средняя оценка выше у { Petr_Lecturer.name} {Petr_Lecturer.surname}')
else:
    print(f' Средние баллы {Ivan_Lecturer.name} {Ivan_Lecturer.surname} и { Petr_Lecturer.name} { Petr_Lecturer.surname} равны')

all_lecturer = [Ivan_Lecturer, Petr_Lecturer]
course = input('\n Введите курс, по которому нужно вычислить средний бал у всех студентов (Python или Git): ')
grade_course_st = AverageGradeCourseSt(all_student, course)
print (f'Средний бал за дз по всем сутдентам в рамках курса {course}: {grade_course_st:0.1f}')
grade_course_st = AverageGradeCourseLt(all_lecturer, 'Python')
print (f'Средний бал за лекции всех лекторов в рамках курса Python (общий курс для лекторов только этот): {grade_course_st:0.1f}')