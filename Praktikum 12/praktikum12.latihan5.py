# Nama    : Dyas Arum Paramitha
# NIM     : J0403251092
# Kelas   : A2
# Praktikum 12 - Graph II: Dijkstra

# ==========================================================
# Program: Jalur Terpendek Antar Kota (Dijkstra)
# ==========================================================

import heapq

# 1. Representasi graph berbobot
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):

    # Menyimpan jarak awal semua node (infinity)
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue untuk memproses node dengan jarak terkecil
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika sudah ada jarak lebih kecil, lewati
        if current_distance > distances[current_node]:
            continue

        # Mengecek semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jalur lebih pendek, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# 3. Input node awal (atau bisa langsung ditentukan)
start_node = input("Masukkan node awal (contoh: Bogor): ")

# 4. Menjalankan algoritma
hasil = dijkstra(graph, start_node)

# 5. Output hasil
print("Jarak terpendek dari {start_node}:")

for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")

# Jawaban Analisis:
# 1. Node awal yang digunakan apa? Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal? Depok dengan jarak 2

# 3. Node mana yang memiliki jarak paling besar dari node awal? Bandung dengan jarak 8

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Dijkstra bekerja dengan memilih node dengan jarak paling kecil dari node awal,
# kemudian memperbarui jarak ke semua tetangga jika ditemukan jalur yang lebih pendek.
# Proses ini diulang menggunakan priority queue sampai semua node diproses,
# sehingga diperoleh jarak terpendek dari Bogor ke semua node lainnya.