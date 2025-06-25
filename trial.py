"""
# 🧠 Challenge: Student and Classroom Performance Tracker

Create a class: `Student`

---

P1

## `Student` Class

**Attributes:**
- `name`: Student's name (string)
- `student_id`: Unique ID (string or int)
- `grades`: Dictionary mapping subject names to a list of grades  

**Methods:**
- `add_grade(subject, grade)`: Adds a valid grade (0–100) to a subject
- `get_average`:
  - If `subject` is provided, returns the average for that subject  
  - If `subject` is not provided, returns the average across all subjects (95.0%)
- `__str__()`: String summary of student name, ID, and average grade

Implement input validation: grades must be between 0–100.

"""

from itertools import chain

class Student:
    def __init__(self, name, student_id, grades) -> None:
        # parse data in
        if not isinstance(name, str):
            raise Exception("name is not string!")

        if not isinstance(student_id, (str, int)):
            raise Exception("student_id is not string or int!")
        
        if isinstance(grades, dict):
            for key in grades.keys():
                if not isinstance(key, str):
                    raise Exception("key in grades is malformed!")
                
        # add data to members
        self.name = name
        self.student_id = student_id
        self.grades = grades
        self.averages = {}

        # validate data!
        # validate grades


    def add_grade(self, subject, grade):
        # adding grade to list in dict
        # error handle
        self.grades[subject].append(grade)

    def get_average(self, subject=None) -> float:
        total = 0
        if not subject:
            combined = list(chain(self.grades.values()))
            total = sum(combined[0])
            return round(total / len(combined[0]), 1)
        
        total = sum(self.grades[subject])
        return round(total / len(self.grades[subject]), 1)

    def __str__(self):
        # String summary of student name, ID, and overall GPA
        ret = []
        ret.append(self.name)
        ret.append(", ")
        ret.append(str(self.student_id))
        ret.append(", ")
        ret.append(str(self.get_average()))

        return ''.join(ret)


student = Student('Al', 123, {'Math': [100, 95]})
print(student)
print(student.get_average())

"""
---

P2

## `Classroom` Class

**Attributes:**
- `students`: A list of `Student` objects
- `subjects`: A set of strings

**Methods:**
- `new_subject(subject)`: Adds a `Subject` to the classroom
- `add_student(student)`: Adds a `Student` to the classroom
- `new_subject(subject)`: Removes a `Subject` from the classroom
- `add_student(student)`: Removes a `Student` from the classroom
- `best_student(subject)`: Returns the `Student` with the highest average in the class and/or subject
- `worst_student(subject)`: Returns the `Student` with the lowest average in the class and/or subject
```

Implement input validation: 
- Students may not have the same identifier.
"""


"""
P3:

`Student.remove_subject(subject)`: Allows for removal of a subject and its grades.
Implement input validation: 
- Students may only have grades in the current subjects offered.


s1 = Student(name = 'Alice', student_id = 103131)

get_average(self, subject=None) -> float:
    grades = self.grades[subject] if subject != None else list(chain(self.grades.values()))
    return round(100 * sum(grades) / len(grades), 1)
"""
