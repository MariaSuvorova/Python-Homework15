import pytest
from student import Student


@pytest.fixture
def student():
    return Student("Иван Иванов", 'subjects.csv')


def test_student_init(student):
    """Initializing a class instance"""
    assert student.name == 'Иван Иванов'


def test_student_init_with_Err():
    """Initializing a class instance with wrong name"""
    with pytest.raises(ValueError):
        Student("Иван1 иванов", 'subjects.csv')


def test_add_grade(student):
    subject = "Математика"
    student.add_grade(subject, 4)
    assert student.subjects[subject]['grades'][0] == 4


def test_add_grade_with_Err_subj(student):
    subject = "Химия"
    with pytest.raises(AttributeError):
        student.add_grade(subject, 4)


def test_add_grade_with_Err_grade(student):
    subject = "Математика"
    with pytest.raises(ValueError):
        student.add_grade(subject, 7)


def test_add_test_score(student):
    subject = "История"
    student.add_test_score(subject, 92)
    assert student.subjects[subject]['test_scores'][0] == 92


def test_add_test_score_with_Err_grade(student):
    subject = "История"
    with pytest.raises(ValueError):
        student.add_test_score(subject, 120)


def test_get_average_test_score(student):
    subject = "Физика"
    student.add_test_score(subject, 92)
    student.add_test_score(subject, 65)
    assert student.get_average_test_score(subject) == 78.5


def test_get_average_grade(student):
    subject = ['Математика', 'Физика', 'История']
    student.add_grade(subject[0], 5)
    student.add_grade(subject[1], 4)
    student.add_grade(subject[2], 3)
    assert student.get_average_grade() == 4


if __name__ == '__main__':
    pytest.main(['-vv'])
