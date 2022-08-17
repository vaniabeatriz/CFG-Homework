"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random


class CFGStudent:
    def __init__(self, name: str, surname: str, age: int, email: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = self.generate_id()

    @staticmethod
    def generate_id():
        rand_id = random.randint(1000, 10000)
        return str(rand_id)

    def get_id(self):
        return self.student_id

    def get_fullname(self):
        return f'{self.name} {self.surname}'


class NanoStudent(CFGStudent):
    def __init__(self, specialization, name, surname, age, email):
        super().__init__(name, surname, age, email)
        self.specialization = specialization
        self.course_grades = {}

    @staticmethod
    def generate_id():
        rand_id = random.randint(1000, 10000)
        return f'NANO{rand_id}'

    def add_new_grade(self, course, grade):
        self.course_grades[course] = grade

    def get_course_grades(self):
        return self.course_grades


s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
print(s.generate_id())

cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
print(cfg_s.get_id())

############################################

# Example run
# s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
# print(s.get_fullname())
# returns 'Anna Smith'
# print(s.student_id)
# returns '3868' or some other random number

# cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
# print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
# print(cfg_s.get_id())
# returns 'NANO6180' or some other random number
# cfg_s.add_new_grade('theory', 95)
# cfg_s.add_new_grade('project', 78)
# print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}


"""

TASK 2
Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence
and return the sum of all even Fibonacci numbers. See more details in the task description in
your assessment paper.

"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_list(elements):
    fib_list = []
    for i in range(elements):
        fib_list.append(fibonacci(i))
    return fib_list

def even_fibonacci_sum(limit):
    fib_list = fibonacci_list(limit)
    even_fib_list = [n for n in fib_list if n % 2 == 0]
    return sum(even_fib_list)

even_fibonacci_sum(10)
print(even_fibonacci_sum(10))

##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))  # should be 0

"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 

"""


def is_valid_subsequence(array, sequence):
    for i in sequence:
        try:
            idx = array.index(s)
        except:
            return False


##### TESTS ####


array1 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence1 = [1, 6, -1, -2]

print(is_valid_subsequence(array1, sequence1))  # FALSE

array2 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence2 = [1, 6, -1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE

array3 = [5, 1, 22, 25, 6, -1, 8, 10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE

"""
# TASK 4
#
# WRITTEN ASSIGNMENT
#
# Write a review on how 'class Employee' can be improved.
# (See PDF document with the code example)
# """


'''
In the remove_employee method I would delete the employee using only the ID, I think the name may be unnecessary.
In the print_employee_report I would use 'a' to add a new line instead of 'w' so we don't overwrite the file.
'''