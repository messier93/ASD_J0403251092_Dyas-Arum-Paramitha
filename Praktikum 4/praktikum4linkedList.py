#================================
#Nama   : Dyas Arum Paramitha 
#NIM    : J0403251092
#Kelas  : TPL A2
#================================

#==========================================
#Implementasi Dasar: Node pada Linked List
#==========================================

class Node:
    #konstruktor yg dijalankan scr otomatis ketika class Node dipanggil/instantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai/data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya 

#1) membuat node dgn instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#2) mendefinisikan head dan menghubungkan node a>b>c>none
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#3) traversal: menelusuri node dari head to None
current = head
while current is not None:
    print(current.data) #show current data on node
    current = current.next #pindah ke note selanjutnya