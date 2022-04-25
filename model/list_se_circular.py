from .node import Node
from .student import Student

class ListSE_circular:
    def __init__(self):
        self.head = None

    def validate_exist(self, id:str):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False

    def add_circular(self, data:Student):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya esta en la lista el estudiante con la identificacion")
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = Node(data)
            temp.next.next = self.head

    def add_to_start_circular(self, data):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya esta en la lista el estudiante con la identificacion")
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = Node(data)
            temp.next.next = self.head
            self.head = temp.next

    def count(self):
        count = 0
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            count += 1

    def get_all_students_circular(self):
        temp = self.head
        list = []
        while temp.next != self.head:
            list.append(temp.data)
            temp = temp.next
        list.append(temp)
        return list





