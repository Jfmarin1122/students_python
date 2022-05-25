from .node import Node
from .student import Student

class ListDECircular:
    def __init__(self):
        self.head = None
        self.count = 0

    def get_all_students_de_circular(self):
        if self.head is not None:
            temp = self.head
            list_students = []
            while temp.next is not self.head:
                list_students.append(temp.data)
                temp = temp.next
            list_students.append(temp.data)
            return list_students

    def validate_exist(self, id: str):
        temp = self.head
        while temp.next is not self.head:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False

    def add_de_circular(self, data: Student):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya esta en la lista el estudiante con la identificacion")
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            node = Node(data)
            temp.next = node
            node.prev = temp
            node.next = self.head
            self.head.prev = node

    def add_to_start_de_circular(self, data: Student):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya esta en la lista el estudiante con la identificacion")
            node = Node(data)
            node.next = self.head
            node.prev = self.head.prev
            node.prev.next = node
            self.head.prev = node
            self.head = node

    def count_de_circular(self):
        count = 0
        temp = self.head
        while temp.next is not self.head:
            temp = temp.next
            count += 1
        count += 1
        return count