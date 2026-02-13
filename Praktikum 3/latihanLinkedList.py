# Dyas Arum Paramitha J0403251092 A2 
# Latihan 1: Implementasikan fungsi untuk menghapus node dengan nilai tertentu.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("No elements.")
            return

        prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

#testingggggggggggggggggg
ll = LinkedList()

ll.insert_at_end(99)
ll.insert_at_end(67)
ll.insert_at_end(29)

print("Before: ")
ll.display()

ll.delete_node(67)

print("After: ")
ll.display()

#Latihan 2: Buat kode Implementasikan Pencarian pada node tertentu Single Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def search(self, key):
        if not self.head:
            print("null")
            return

        temp = self.head

        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam circular linked list.")
                return

            temp = temp.next

            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam list.")

    def display(self):
        if not self.head:
            print("null.")
            return

        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("... (back to head)")


#test
cll = CircularSinglyLinkedList()
cll.insert_at_end(3)
cll.insert_at_end(7)
cll.insert_at_end(12)
cll.insert_at_end(19)
cll.insert_at_end(25)

cll.display()
cll.search(12)

#Latihan 4: Buat metode untuk menggabungkan dua single linked list menjadi satu linked list baru.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, list2):
        if not self.head:
            return list2

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = list2.head
        return self

# testt
ll1 = LinkedList()
ll2 = LinkedList()

#lsit1
for i in [1, 3, 5, 7]:
    ll1.insert_at_end(i)

#list2
for i in [2, 4, 6, 8]:
    ll2.insert_at_end(i)

print("Linked list 1: ")
ll1.display()

print("Linked list 2:" )
ll2.display()

# Gabungkan
merged = ll1.merge(ll2)

print("Linked List setelah digabung: ")
merged.display()