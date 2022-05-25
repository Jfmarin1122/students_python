from model.student import Student
from model.list_de_circular import ListDECircular

class ListDEcircular_service:
    cities = ['Manizales', 'Pereira', 'Chinchina', 'Armenia']
    def __init__(self):
        self.students = ListDECircular()

    def get_all_students_de_circular(self):
        if self.students.head is None:
            return {"message": "La lista esta vacia"}
        else:
            return self.students.get_all_students_de_circular()

    def add_student_de_circular(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_de_circular(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def add_student_to_start_de_circular(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_start_de_circular(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def count_de_circular(self):
        if self.students.head is None:
            return {"message": "La lista esta vacia"}
        return {"la cantidad de estudiantes es": self.students.count_de_circular()}