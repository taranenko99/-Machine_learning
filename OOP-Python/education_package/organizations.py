import csv
from education_package.users import *

class School:
    def __init__(self, name=None, address=None, phone=None, email=None, num_stud=None, num_teachers=None):
        self._sname = name
        self._address = address
        self._phone = phone
        self._email = email
        self._num_stud = 0
        self._num_teachers = 0
        self._students = []
        self._teachers = []

    def set_name(self, name):
        self._sname = name
        pass

    def set_address(self, address):
        self._address = address
        pass

    def set_phone(self, phone):
        self._phone = phone
        pass

    def set_email(self, email):
        self._email = email
        pass

    def set_num_stud(self, num_stud):
        self._num_stud = num_stud
        pass

    def set_num_teachers(self, num_teachers):
        self._num_teachers = num_teachers
        pass

    def add_student(self, name=None, familyname=None, age=None, gender=None, nationality=None, subject=None):
        is_student_already_exists = False
        for idx,student in enumerate(self._students):
            if (student._name == name) and (student._familyname == familyname) and (student._age == age) and (student._gender == gender) and (student._nationality == nationality):
                is_student_already_exists = True
                break

        if not is_student_already_exists:
            self._num_stud += 1
            self._students.append(Student(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality, school=self._sname, subject=subject))

    def add_teacher(self, name=None, familyname=None, age=None, gender=None, nationality=None, subject=None):
        is_teacher_already_exists = False
        for idx, teacher in enumerate(self._teachers):
            if (teacher._name == name) and (teacher._familyname == familyname) and (teacher._age == age) and (teacher._gender == gender) and (teacher._nationality == nationality):
                is_teacher_already_exists = True
                break

        if not is_teacher_already_exists:
            self._num_teachers += 1
            self._teachers.append(Student(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality, school=self._sname, subject=subject))

    def get_info(self):
        return {"name": self._sname, "address": self._address, "phone": self._phone, "email": self._email, "num_stud": self._num_stud, "num_teachers": self._num_teachers}

    def get_report(self):
        with open(f"{self._sname}_report.csv", mode="w", newline="", encoding="UTF-8") as file:
            writer = csv.writer(file)
            info = self.get_info()
            for key, value in info.items():
                writer.writerow([f"{key}:{value}"])

            for student in self._students:
                s = student.get_info()
                for key, value in s.items():
                    writer.writerow([f"{key}:{value}"])

            for teacher in self._teachers:
                t = teacher.get_info()
                for key, value in t.items():
                    writer.writerow([f"{key}:{value}"])
