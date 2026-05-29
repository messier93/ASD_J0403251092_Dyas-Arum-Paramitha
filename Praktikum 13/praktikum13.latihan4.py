# Nama    : Dyas Arum Paramitha
# NIM     : J0403251092
# Kelas   : A2
# Praktikum 13 - Graph III: Spanning Tree

# ==========================================================
# Studi Kasus: Jaringan Kabel Antar Gedung dengan Algoritma Kruskal
# ==========================================================

# Daftar edge: (bobot, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

# Set untuk menyimpan node yang sudah terhubung
connected = set()

# Proses pemilihan edge
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total biaya minimum =", total_weight)


# Jawaban Analisis
# 1. Algoritma apa yang digunakan? Algoritma yang digunakan adalah Kruskal.

# 2. Edge mana saja yang dipilih? Edge yang dipilih adalah:
# GedungC - GedungD = 1
# GedungA - GedungC = 2
# GedungB - GedungD = 3

# 3. Berapa total biaya minimum? Total biaya minimum yang dihasilkan adalah 6.

# 4. Mengapa MST cocok digunakan pada kasus ini? Karena MST dapat menghubungkan semua gedung dengan biaya
# pemasangan kabel paling minimum tanpa membentuk cycle.