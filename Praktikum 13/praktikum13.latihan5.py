# Nama    : Dyas Arum Paramitha
# NIM     : J0403251092
# Kelas   : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Tugas Mandiri: Jaringan Komputer dengan Kruskal
# ==========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

# Set sederhana untuk node yang sudah dipilih
connected = set()

for weight, u, v in edges:
    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis
# 1. Kasus apa yang dipilih? Kasus yang dipilih adalah Jaringan Komputer.

# 2. Algoritma apa yang digunakan? Algoritma yang digunakan adalah Kruskal.

# 3. Edge mana saja yang dipilih dalam MST? Edge yang dipilih adalah:
# RouterC - RouterD = 1
# RouterA - RouterC = 2
# RouterA - RouterB = 3

# 4. Berapa total bobot MST? Total bobot MST yang dihasilkan adalah 6.

# 5. Mengapa edge tertentu tidak dipilih? Karena edge tersebut memiliki bobot lebih besar atau dapat membentuk cycle.