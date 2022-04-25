from model.student import Student
from model.list_se import ListSE
from model.list_se_circular import ListSE_circular

class list_se_circular_service:
    def add_circular(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def add_to_start_circular(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_start(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def get_all_students_circular(self):
        return self.student.get_all_students_circular()

    def count(self):
        pass
