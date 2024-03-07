import csv
from student_logger import log_decorator, for_all_methods


@for_all_methods(log_decorator)
class Student:
    def __init__(self, name: str, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __setattr__(self, name: str, value: str):
        if name == 'name':
            if not (value.istitle() and value.replace(' ', '').isalpha()):
                raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f'Предмет {name} не найден')  

    def __str__(self):
        str_subj = list()
        for subj in self.subjects.keys():
            if len(self.subjects[subj]['grades']) != 0 or len(self.subjects[subj]['test_scores']) != 0:
                str_subj.append(subj)
        subjects = ', '.join(str_subj)
        return f'Студент: {self.name}\nПредметы: {subjects}'

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', encoding='utf-8') as file:
            for line in csv.reader(file, delimiter=','):
                for subject in line:
                    if subject not in self.subjects:
                        self.subjects[subject] = {'grades': [], 'test_scores': []}
        return self.subjects

    def add_grade(self, subject, grade): 
        if subject in self.subjects:
            if isinstance(grade, int) and 2 <= grade <= 5:
                self.subjects[subject]['grades'].append(grade)
            else: 
                raise ValueError('Оценка должна быть целым числом от 2 до 5')  
        else:
            raise AttributeError(f'Предмет {subject} не найден') 
        
    def add_test_score(self, subject, test_score):
        if subject in self.subjects:
            if isinstance(test_score, int) and 0 <= test_score <= 100:
                self.subjects[subject]['test_scores'].append(test_score)
            else:
                raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        else:
            raise AttributeError(f'Предмет {subject} не найден') 
        
    def get_average_test_score(self, subject): 
        if subject not in self.subjects:
            raise ValueError(f'Предмет {subject} не найден')
        else:
            test_scores = self.subjects[subject]['test_scores']
            if len(test_scores) == 0:
                return 0
            else:
                return sum(test_scores)/len(test_scores)

    def get_average_grade(self):
        sub_grade = []
        for subject in self.subjects:
            sub_grade.extend(self.subjects[subject]['grades'])
        if len(sub_grade) == 0:
            return 0
        else:
            total_average = sum(sub_grade)/len(sub_grade)
        return total_average
