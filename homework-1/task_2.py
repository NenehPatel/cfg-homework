
"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id, subject):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = {
            "name": name,
            "subject":subject
        }

class CFGstudent(Student):

    def __init__(self, name, age, id, subject):
        super().__init__()
    def add_subject(self, subject):
        self.subjects = {}
        self.subjects.update({"subject"}) == subject
        print(f"A subject {self.subjects[1]} has been added to your timetable.")

    def remove_subject(self, subject):
        self.subjects = {}
        self.subjects.pop(subject)
        print(f"A subject {self.subjects[subject]} has been removed from your timetable.")

    def view_all_subjects(self):
        print(f"This student is studying {self.subjects}")

    def add_grade(self, name, subject_one, grade_one):
        self.grades = {
            "name":name,
            "subject 1":subject_one,
            "grade 1":grade_one,
            "subject 2": subject_two,
            "grade 2":grade_two,
            "subject 3": subject_three,
            "grade 3":grade_three
        }
        self.grades.append(name, subject_one, grade_one)
        print("You have added the student called {name} to the subject {subject_one} with the grade {grade_one}")


    def overall_grades(self, name, grade_one, grade_two, grade_three, subject_one, subject_two, subject_three):
        if grade_one>0 and grade_two>0 and grade_three>0:
            print(f"The student called {name} has an overall grade of {(grade_one+grade_two+grade_three)/3} across {subject_one}, {subject_two} and {subject_three}.")
        elif grade_one>0 and grade_two>0:
            print(f"The student called {name} has an overall grade of {(grade_one+grade_two)/2}")
        else grade_one>0:
            print(f"The student called {name} does not study enough subjects to find their overall grade.")

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


student1 = Student(name="Suraiya", age=27, id=1248,subject="Software")