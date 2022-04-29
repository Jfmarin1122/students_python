class Student:
   """ def __init__(self,identification,gender, salary,job,name, age, zona_rural, city):
        self.identification = identification
        self.gender = gender
        self.salary = salary
        self.job = job
        self.name = name
        self.age = age
        self.zona_rural = zona_rural
        self.city = city
        """
   def __init__(self, my_dict):
       if self.validar_datos(my_dict) == True:
           for key in my_dict:
               setattr(self, key, my_dict[key])
       else:
           raise Exception("Faltan algunos atributos")

   def validar_datos(self, my_dict):
       attributes = ["identification", "gender", "salary", "job", "name", "age", "zona_rural", "city"]
       keys = list(my_dict.keys())
       return keys == attributes
