from student import Student
from csv_parser import csv_parser

# Проверка логирования

# python __main__.py subjects.csv
file_name = csv_parser()

student = Student("Иван Иванов", file_name)
student2 = Student("Иван1 иванов", file_name)

student.add_grade("Математика", 7)

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("Химия", 4)

student.add_grade("История", 5)
student.add_test_score("История", 92)

student.add_test_score("История", 120)

average_grade = student.get_average_grade()

average_test_score = student.get_average_test_score("Математика")
