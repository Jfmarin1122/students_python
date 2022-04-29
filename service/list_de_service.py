from model.student import Student
from model.list_de import ListDE

class ListDEservice:
    cities = ['Manizales', 'Pereira', 'Chinchina', 'Armenia']
    def __init__(self):
        self.students = ListDE()

    def get_all_students(self):
        if self.students.head == None:
            return {"message":"La lista esta vacia"}
        else:
            return self.students.get_all_students()

    def add_student(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_student(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def add_to_start(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_start(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def count(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        return {"la cantidad de estudiantes es": self.students.count()}