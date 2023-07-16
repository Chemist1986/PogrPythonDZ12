import csv

class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name
    
    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError("Недопустимый формат имени. Допускаются только алфавитные символы с заглавной первой буквой.")
        instance._name = value

class SubjectDescriptor:
    def __init__(self, subjects_file):
        self.subjects = self.load_subjects(subjects_file)
    
    def load_subjects(self, file):
        with open(file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            subjects = next(reader, [])
        return subjects
    
    def __get__(self, instance, owner):
        return self.subjects
    
    def __set__(self, instance, value):
        raise AttributeError("Нельзя изменять темы напрямую. Используйте метод 'add_score.")

class Student:
    name = NameDescriptor()
    subjects = SubjectDescriptor('subjects.csv')
    
    def __init__(self):
        self.scores = {subject: {'оценки': [], 'результаты теста': []} for subject in self.subjects}
    
    def add_score(self, subject, grade, test_result):
        if subject not in self.subjects:
            raise ValueError(f"{subject} это неподходящий предмет для данного студента.")
        
        if grade < 2 or grade > 5:
            raise ValueError("Недопустимая оценка. Допускаются только значения от 2 до 5.")
        
        if test_result < 0 or test_result > 100:
            raise ValueError("Неверный результат теста. Допускаются только значения от 0 до 100.")
        
        self.scores[subject]['оценки'].append(grade)
        self.scores[subject]['результат теста'].append(test_result)
    
    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"{subject} это неподходящий предмет для данного студента.")
        
        test_results = self.scores[subject]['результат теста']
        if not test_results:
            return 0
        
        return sum(test_results) / len(test_results)
    
    def get_average_grades(self):
        all_grades = []
        for subject in self.subjects:
            all_grades.extend(self.scores[subject]['оценки'])
        
        if not all_grades:
            return 0
        
        return sum(all_grades) / len(all_grades)
student = Student()
student.name = "Ivan Drago"



student.add_score('Математика', 4, 80)
student.add_score('Математика', 3, 75)
student.add_score('Английский', 5, 90)
student.add_score('Английский', 4, 85)



math_average = student.get_average_test_score('Математика')
english_average = student.get_average_test_score('Английский')
print(f"Средний балл теста по математике: {math_average}")
print(f"Средний балл теста по английскому языку: {english_average}")



average_grades = student.get_average_grades()
print(f"Средние оценки по всем предметам: {average_grades}")


