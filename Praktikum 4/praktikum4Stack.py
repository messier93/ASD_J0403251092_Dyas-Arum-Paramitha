#================================
#Nama   : Dyas Arum Paramitha 
#NIM    : J0403251092
#Kelas  : TPL A2
#================================

#==========================================
#Implementasi Dasar: Stack 
#==========================================

class Node:
    #konstruktor yg dijalankan scr otomatis ketika class Node dipanggil/instantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai/data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya 

#Stack ada operasi push (memasukkan head baru) n pop (menghapus head)
# A>B>C>None

class stack:
    def __init__(self):
        self.head = None #head menunjuk ke node plg atas (awalnya kosong)
    
    def push(self,data):
        #1) membuat node baru
        nodeBaru = Node(data) #instantiasi/memanggil konstruktor pd class Node
        #2) node baru hrs menunjuk ke head yang lama
        nodeBaru.next = self.head
        #3)geser head ke node baru
        self.head = nodeBaru
        #B>A>None
    
    def is_empty(self):
        return self.head is None #stack bkosong jika head = None

    def pop(self): #mengambil/delete head node

        if self.is_empty():
            print("Stack kosong, tidak bisa pop.")
            return None
        deletedData = self.head.data #soroti bagian head dan save di variabel (peek)
        #B>A>None
        self.head = self.head.next #geser head ke node berikutnya
        return deletedData #kembalikan data yg dihapus

    def peek(self):
        #melihat data yg paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.head.data

    def tampilkan(self):
        #Top -> A -> B
        current = self.head
        print("Top->", end=" ")
        while current is not None:
            print(current.data, end="-> ")       
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek a boo! (Look for head): ", s.peek())
s.pop()
s.tampilkan()
print("Peek a boo! (Look for head): ", s.peek())