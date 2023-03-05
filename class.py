class Zajecia:
    def __init__(self):
        self.list_of_students = []

    def add_student(self, name):
        if len(self.list_of_students) < 10:
            self.list_of_students.append(name)
            print("Student added")
        else:
            print("Cannot add another student")

zajecia = Zajecia()
zajecia.add_student("Mark")
zajecia.add_student("John")
zajecia.add_student("Pablo")
zajecia.add_student("Ann")
zajecia.add_student("Adrew")
zajecia.add_student("Mary")
zajecia.add_student("Elizabeth")
zajecia.add_student("Anthony")
zajecia.add_student("Peter")
zajecia.add_student("Camilla")
zajecia.add_student("Baby John")
print(f"{zajecia.list_of_students}, {len(zajecia.list_of_students)} people")
