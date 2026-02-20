#================================
#Nama   : Dyas Arum Paramitha 
#NIM    : J0403251092
#Kelas  : TPL A2
#================================

#==========================================
#Implementasi Dasar: Queue
#==========================================

class Node:
    #konstruktor yg dijalankan scr otomatis ketika class Node dipanggil/instantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai/data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya 
    
class queue:
    #buat konstruktor untuk insiialisasi variabel front n rear
    def  __init__(self):
        self.front = None #head plg depan
        self.rear = None #head plg blkg

    def is_empty(self):
        return self.front is None

    #membuat fungsi utk menambahkan data baru
    def enqueue(self,data):
        nodeBaru = Node(data)

        #if queue is empty, front n rear menunjukkan ke node yg sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #if queue is NOT empty, maka letakkan new data ke after rear dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #letakkan data baru pd after rear
        self.rear = nodeBaru #jadikan data baru sbg rear

    def dequeue(self):
        #hapus data dr depan/front
        deletedData = self.front.data #lihat data plg depan
        #geser front ke node berikutnya
        self.front = self.front.next
        #jika after geser front mnjd none, maka queue kosong dan rear jg hrs jd None
        if self.front is None:
            self.rear = None
        return deletedData
    
    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end="-> ")
            current = current.next
        print(" Rear")

#instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()