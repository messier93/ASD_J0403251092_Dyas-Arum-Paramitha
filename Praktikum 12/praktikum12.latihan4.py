# Nama    : Dyas Arum Paramitha
# NIM     : J0403251092
# Kelas   : A2

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


hasil = dijkstra(graph, 'Gerbang')

print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang? Kantin, dengan waktu tempuh 2 menit.

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula? 7 menit (Gerbang -> Kantin -> Lab -> Aula).

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan. Tidak. Jalur langsung tidak 
# selalu paling kecil karena bisa saja jalur tidak langsung memiliki total bobot (waktu) yang lebih kecil 
# dibanding jalur langsung, seperti Gerbang -> Aula (tidak langsung) lebih cepat dibanding rute lain yang 
# lebih panjang namun berbobot kecil.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini? Karena Dijkstra efektif untuk mencari 
# jalur terpendek pada graph berbobot positif seperti waktu tempuh antar lokasi kampus, sehingga dapat 
# menentukan rute tercepat secara akurat dan efisien.