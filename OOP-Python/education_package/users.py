class Human:
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None):
        self._name = name
        self._familyname = familyname
        self._age = age
        self._gender = gender
        self._nationality = nationality

    def set_name(self, name):
        self._name = name
        pass

    def set_family(self, familyname):
        self._familyname = familyname
        pass

    def set_age(self, age):
        self._age = age
        pass

    def set_gender(self, gender):
        self._gender = gender
        pass

    def set_nationality(self, nationality):
        self._nationality = nationality
        pass

    def get_info(self):
        return {"name": self._name, "familyname": self._familyname, "age":self._age, "gender": self._gender, "nationality": self._nationality}

class Student(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subject=None):
        Human.__init__(self, name=name, familyname=familyname, age=age, gender=gender, nationality=nationality)
        self._school = school
        self.subject = subject
        self.list_of_items = []

    def set_school(self, school):
        self._school = school
        pass

    def add_subject(self, subject):
        self.list_of_items.append(subject)

    def get_info(self):
        info_student = dict()
        info_student.update(super().get_info())
        info_student.update({"school": self._school, "subject": self.subject})

        return info_student

class Teacher(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, subject=None):
        Human.__init__(self, name=name, familyname=familyname, age=age, gender=gender, nationality=nationality)
        self._school = school
        self.subject = subject
        self.list_of_subject_teacher = []

    def set_school(self, school):
        self._school = school
        pass

    def add_subject(self, subject):
        self.list_of_subject_teacher.append(subject)

    def get_info(self):
        info_teacher = dict()
        info_teacher.update(super().get_info())
        info_teacher.update({"school": self._school, "subject": self.subject})

        return info_teacher