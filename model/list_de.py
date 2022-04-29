from .node import Node
from .student import Student

class ListDE:
    def __init__(self):
        self.head = None

    def get_all_students(self):
        list = []
        temp = self.head
        while temp.next != None:
            list.append(temp.data)
            temp = temp.next
        list.append(temp.data)
        return list

    def validate_exist(self, id: str):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False

    def add_student(self, data:Student):
        node = Node(data)
        if self.head == None:
            if self.validate_exist(data.identification):
                raise Exception("Ya esta en la lista el estudiante con la identificacion")
            self.head = node
        else:
            anterior = self.head
            while anterior.next != None:
                anterior = anterior.next
            if self.validate_exist(data.identification):
                raise Exception("Ya esta en la lista el estudiante con la identificacion")
            anterior.next = node
            node.prev = anterior

    def add_to_start(self, data: Student):
        node = Node(data)
        if self.head == None:
            self.head = node

        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya esta en la lista el estudiante con la identificacion")
            node.next = self.head
            self.head.prev = node
            self.head = node

    def count(self):
        pass