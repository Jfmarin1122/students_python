from .node import Node
from .student import Student

class ListDE:
    def __init__(self):
        self.head = None

    def get_all_students(self):
        list = []
        temp = self.head
        while temp.next is not None:
            list.append(temp.data)
            temp = temp.next
        list.append(temp.data)
        return list

    def validate_exist(self, id: str):
        temp = self.head
        while temp is not None:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False

    def add_student(self, data: Student):
        if self.validate_exist(data.identification):
            raise Exception("Ya esta en la lista el estudiante con la identificacion")
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.prev = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp

    def add_to_start(self, data: Student):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.prev = None
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya esta en la lista el estudiante con la identificacion")
            node.next = self.head
            self.head.prev = node
            self.head = node

    def count(self):
        count = 0
        temp = self.head
        while temp.next != None:
            temp = temp.next
            count += 1
        count += 1
        return count

    def invert_list(self):
        if self.head != None:
            list_copy = ListDE()
            temp = self.head
            while temp != None:
                list_copy.add_to_start(temp.data)
                temp = temp.next
            self.head = list_copy.head

    def head_finish(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        dateTemporal = self.head.data
        self.head.data = temp.data
        temp.data = dateTemporal

    def mujeres_primero(self):
        lista_copia = ListDE()
        if self.head == None:
            return None
        temp = self.head
        while temp != None:
            if temp.data.gender == 1:
                lista_copia.add_student(temp.data)
            else:
                lista_copia.add_to_start(temp.data)
            temp = temp.next
        self.head = lista_copia.head

    def intercalar_gender(self):
        list_man = ListDE()
        list_woman = ListDE()
        count_man = 0
        count_woman = 0
        list_comparar_genero = ListDE()
        temp = self.head
        while temp is not None:
            if temp.data.gender == 1:
                list_man.add_student(temp.data)
                count_man = count_man + 1
            elif temp.data.gender == 2:
                count_woman = count_woman + 1
                list_woman.add_student(temp.data)
            temp = temp.next
        if count_man > count_woman:
            mayorLongitud = count_man
        else:
            mayorLongitud = count_woman
        temp_man = list_man.head
        temp_woman = list_woman.head
        while mayorLongitud > 0:
            if temp_woman is not None:
                list_comparar_genero.add_student(temp_woman.data)
                temp_woman = temp_woman.next
            if temp_man is not None:
                list_comparar_genero.add_student(temp_man.data)
                temp_man = temp_man.next
            mayorLongitud = mayorLongitud - 1
        self.head = list_comparar_genero.head           # Actualizar cabeza

    def delete_by_data(self, id: str):
        if self.head is None:
            return None
        actual = self.head
        while actual.data.identification != id and actual.next is not None:
            actual = actual.next
        if actual.data.identification == id:
            if actual is self.head:
                if actual.next is not None:
                    self.head = actual.next
                    self.head.prev = None
                else:
                    self.head = None
            else:
                anterior = actual.prev
                anterior.next = actual.next
            return actual
        else:
            return None

    def delete_by_position(self, position: int):
        if self.head is None:
            return None
        count = 0
        actual = self.head
        while actual.next is not None and count is not position:
            actual = actual.next
            count += 1
        if count == position:
            if actual is self.head:
                if actual.next is not None:
                    self.head = actual.next
                    self.head.prev = None
                else:
                    self.head = None
            else:
                anterior = actual.prev
                anterior.next = actual.next
            return actual
        else:
            return None

    def add_to_position(self):
        pass
