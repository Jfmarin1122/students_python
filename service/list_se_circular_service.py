from model.student import Student
from model.list_se_circular import ListSE_circular

class ListSEcircular_service:
    cities = ['Manizales', 'Pereira', 'Chinchina', 'Armenia']
    def __init__(self):
        self.students = ListSE_circular()

    def get_all_students_circular(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            return self.students.get_all_students_circular()

    def add_student_circular(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_student_circular(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def add_student_to_start_circular(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_student_to_start_circular(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def count(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        return {"la cantidad de estudiantes es": self.students.count()}
    