from model.student import Student
from model.list_se import ListSE

class ListSEService:
    cities = ['Manizales', 'Pereira', 'Chinchina', 'Armenia']

    def __init__(self):
        self.students = ListSE()
        """
        jfmarin = Student({"identification":"1002542593", "name": "Juan Felipe",
                           "gender":1, "salary":2000000, "job": True, "edad":21,"Zona_rural":2,
                           "city":self.cities[0]})
        self.students.add(jfmarin)
        self.students.add(Student({"idenfication": "1060456789", "name": "Valentina Hurtado",
                                   "gender": 2, "salary": 0, "job": False, "edad":20, "Zona_rural":1,
                                   "city": self.cities[0]}))"""

    def get_all_students(self):
        return self.students.head     # Retornar el primero de la lista

    # Agregar estudiante desde Postman
    def add_student(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def add_student_to_start(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_start(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def invert(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.students.invert()
            return {"message": "Se ha invertido la lista"}

    def head_finish(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.students.head_finish()
            return {"message": "Se invirtieron los datos de los extremos"}

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

    def add_to_position(self, position, dict):
        try:
            self.students.add_to_position(position, Student(dict))
            return {"message": "Adicionado exitosamente"}
        except Exception as e:
            return {"message": str(e)}