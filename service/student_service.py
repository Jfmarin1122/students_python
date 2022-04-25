import math

from model import student
from model.student import Student
import json

class StudentService:
    def __init__(self):
        self.students = []
        self.cities = ['Manizales', 'Pereira', 'Chinchina', 'Armenia']
        self.students.append(Student({"idenfication": "1002542593", "name": "Juan Felipe",
                                   "gender": 1, "salary":4000000, "job": True, "age": 21,
                                    "zona_rural": 1, "city": self.cities[0]}))
        self.students.append(Student({"identification": "1002591509", "name": "Laura Cardenas",
                                      "gender":2, "salary":3300000, "job":True, "age":19,
                                      "zona_rural":1, "city": self.cities[0]}))
        self.students.append(Student({"idenfication": "1002542593", "name": "Valentina Hurtado",
                                      "gender": 2, "salary": 0, "job": False, "age": 20,
                                      "zona_rural": 2, "city": self.cities[2]}))
        self.students.append(Student({"idenfication": "1093108156", "name": "Laura Alayon",
                                      "gender": 2, "salary": 170000, "job": True, "age": 20,
                                      "zona_rural": 1, "city": self.cities[1]}))
        self.students.append(Student({"idenfication": "1281301314", "name": "Alejandro Libreros",
                                      "gender": 1, "salary": 3000000, "job": True, "age": 20,
                                      "zona_rural": 1, "city": self.cities[3]}))

        """
        self.students.append(Student("363763763", 1, 1500000, True, "Carlos Loaiza", 42, 1, self.cities[2]))
        self.students.append(Student("363766667", 2, 0, False, "Valentina Hurtado", 19, 2, self.cities[3]))
        self.students.append(Student("2336363", 1, 100000, True, "Kevin Sánchez", 28, 1, self.cities[1]))
        self.students.append(Student("1002591", 2, 3300000, True, "Laura Cardenas", 19, 2, self.cities[0]))
        self.students.append(Student("100254", 1, 5000000, True, "Juan Felipe", 21, 1, self.cities[0]))
        self.students.append(Student("17381131", 2, 270000, True, "Laura Alayón", 19, 1, self.cities[3]))
        self.students.append(Student("83193131", 1, 4200000, True, "Alejandro Libreros", 19, 2, self.cities[2]))
       """

    def get_all_students(self):
        return self.students

    def get_percentage_students_by_gender(self, gender):
        count = 0
        for student in self.students:
            if student.gender == gender:
                count = count +1
        return count/ len(self.students)

    def get_percentage_students_job_avg_salary(self, gender):
        count = 0
        sum_salary = 0
        for student in self.students:
            if student.job == True and student.gender == gender:
                count = count + 1
                sum_salary = sum_salary + student.salary
        if count > 0:
            return {"salario promedio": sum_salary/count,
                "cantidad": count,
                "% trabajan": count/len(self.students)}
        else:
            return{"Error": "La consulta no generó resultados"}

    def get_students_mayor_salary(self, gender, salary):
        students_mayor_salary = []
        for student in self.students:
            if student.salary > salary and student.gender == gender:
                students_mayor_salary.append(student)
        if len(students_mayor_salary) > 0:
            return {"salary": salary,
                    "Students": students_mayor_salary}
        else:
            return{"Error": "Ningun estudiante gana mayor salario"}

    def get_gender_mayor_salary(self, gender):
        students_mayor_salary = []
        salary_students = 0
        for student in self.students:
            if student.gender == gender and student.salary > salary_students:
                salary_students = student.salary
                students_mayor_salary = student
        return {"El estudiante que mas gana es": students_mayor_salary}

    def get_rango_salary(self, min, max):
        rango_salary = []
        for student in self.students:
            if student.salary >= min and student.salary <= max:
                rango_salary.append(student)
        return rango_salary

    def get_average_salary_by_gender(self, gender):
        sum_salary = 0
        count_students = 0
        for student in self.students:
            if student.gender == gender:
                count_students += 1
                sum_salary = sum_salary + student.salary
        if count_students > 0:
            return {"salario promedio": sum_salary/count_students}
        else:
            return{"Error": "La consulta no generó resultados"}

    def get_gender_menor_salary(self, gender):
        students_menor_salary = []
        salary_students = math.inf
        for student in self.students:
            if student.gender == gender and student.salary < salary_students:
                salary_students = student.salary
                students_menor_salary = student
        return {"El estudiante que menos gana es": students_menor_salary}

    def get_promedio_edad(self):
        suma_edad = 0
        count_students = 0
        for student in self.students:
            count_students += 1
            suma_edad = suma_edad + student.age
        return suma_edad / count_students

    def get_zona_edadmayor(self):
        self.get_promedio_edad()
        rural_students = []
        count = 0
        for student in self.students:
            mayor_edad_promedio = self.get_promedio_edad()
            if student.zona_rural == True and student.age > mayor_edad_promedio:
                count = count + 1
                rural_students.append(student)
        return {'Viven en rural y su edad es mayor al promedio': rural_students}

    def get_dict_cities(self):
        dict_cities = {}
        for city in self.cities:
            dict_cities[city]=[0,0]
        return dict_cities

    def get_student_by_city(self):
        dict_cities = self.get_dict_cities()
        for student in self.students:
            if student.job == True:
                dict_cities[student.city][0] += 1
            else:
                dict_cities[student.city][1] += 1
        return dict_cities