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

    def invert_list(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.students.invert_list()
            return {"message": "Se ha invertido la lista"}

    def head_finish(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.students.head_finish()
            return {"message": "Se invirtieron los datos de los extremos"}

    def mujeres_primero(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.students.mujeres_primero()
            return {"message": "Lista organizada, mujeres primero"}

    def intercalar_gender(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.students.intercalar_gender()
            return {"message": "Lista intercalada por genero"}

    def delete_by_data(self, id):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            deleted_student = self.students.delete_by_data(id)
            if deleted_student == None:
                return {"message": "El estudiante no esta en la lista"}
            else:
                return {"message": "Se ha eliminado el estudiante de la lista"}

    def delete_by_position(self, position):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            deleted_student = self.students.delete_by_position(position)
            if deleted_student == None:
                return {"message": "Posicion invalida"}
            else:
                return {"message": "Se ha eliminado el estudiante de la lista"}
