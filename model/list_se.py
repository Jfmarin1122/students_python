from .node import Node
from .student import Student

class ListSE:
    def __init__(self):
        self.head = None                                # La cabeza está vacía
        self.count = 0

    # Adicionar al final
    def add(self, data: Student):                       # Añadir elemento al final de la lista.
        if self.head == None:                           # Si la cabeza está vacía.
            self.head = Node(data)                      # Agregar dato al nodo
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya esta en la lista el estudiante con la identificacion")
            temp = self.head                            # se posiciona un ayudante en la cabeza
            while temp.next != None:                    # Mientras ayudante.next esté lleno
                temp = temp.next                        # Ayudante se corre un espacio
            # Posicionados en el último elemento
            temp.next = Node(data)                      # Agregar elemento a la fila
        self.count = +1

    def add_to_start(self, data:Student):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node (data)
            temp.next = self.head
            self.head = temp

    def invert(self):
        if self.head != None:                           # Si hay algo en la cabeza
            list_copia = ListSE()                       # Crear una nueva lista para la invertida
            temp = self.head                            # Pedir un ayudante que se posicione en la cabeza
            while temp != None:                         # Mientras el ayudante esté lleno
                list_copia.add_to_start(temp.data)               # Añadir copia de los datos de la lista principal
                temp = temp.next                        # La copia del dato se adiciona al principio de la lista copia
            self.head = list_copia.head                 # La lista original reemplaza la cabeza por la lista copia.

    # Validar existencia del estudiante por medio de la identificación
    def validate_exist(self, id:str):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False

    def head_finish(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        dateTemporal = self.head.data
        self.head.data = temp.data
        temp.data = dateTemporal

    def delete_by_data(self, id:str):
        if self.head == None:
            return None
        anterior =  self.head
        actual = self.head
        while actual.data.identification != id and actual.next != None:
            anterior = actual
            actual = actual.next
        if actual.data.identification == id:
            if actual is self.head:
                if actual.next != None:
                    self.head = actual.next
                else:
                    self.head = None
            else:
                anterior.next = actual.next
            return actual
        else:
            return None

    def delete_by_position(self, position:int):
        if self.head == None:
            return None
        count = 0
        anterior = self.head
        actual = self.head
        while actual.next != None and count != position:
            anterior = actual
            actual = actual.next
            count += 1
        if count == position:
            if actual is self.head:
                if actual.next != None:
                    self.head = actual.next
                else:
                    self.head = None
            else:
                anterior.next = actual.next
            return actual
        else:
            return None

    def add_to_position(self, position: int, student:Student):
        if position > 0:
            if position == 1:
                self.add_to_start(student)
                if position == self.count:
                    node = Node(student)
                    temp = self.head
                    while temp.next.next != None:
                        temp = temp.next
                    node.next = temp.next
                    temp.next = node
            else:
                ubication = 2
                temp = self.head
                while temp.next != None and position != ubication:
                    ubication = ubication + 1
                    temp = temp.next
                new_node = Node(student)
                if temp.next != None:
                    if self.validate_exist(student.identification):
                        raise Exception("Ya existe un estudiante con esa identificacion")
                    new_node.next = temp.next
                    temp.next = new_node
            self.count = +1
        else:
            raise Exception("La posición no es válida")

    def intercalar_genero(self):
        pass

    def Mujeres_primero(self):
        lista_copia = ListSE()
        if self.head == None:
            return None
        temp = self.head
        while temp.next != None:
            temp = temp.next
            if temp.data.gender == 1:
                lista_copia.add(temp.data)
            else:
                lista_copia.add_to_start(temp.data)
        self.head = lista_copia.head
