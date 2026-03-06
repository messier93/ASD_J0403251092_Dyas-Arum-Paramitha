# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2

# =========================
# Latihan Soal Pengurutan (Menggunakan Merge Sort)
# =========================

"""Pak Budi adalah seorang manager sumber daya manusia di suatu perusahaan. Ia
saat ini harus menseleksi pelamar kerja berdasarkan skor tes potensi akademik
mereka. Skor tersebut disajikan dalam bentuk list dengan rentang nilai 0 - 100.
Berikut adalah data hasil tes potensi akademik yang tersedia:
[43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

Soal:
1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
2. Kandidat berapa saja yang lolos?
"""

# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2

# =========================
# Latihan Soal Pengurutan (Merge Sort)
# =========================

def mergeSort(data):

    if len(data) > 1:
        mid = len(data)//2
        left = data[:mid]
        right = data[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1


data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

mergeSort(data)

print("Data setelah diurutkan: ", data)

# ambil 5 nilai tertinggi
topFive = data[-5:]
topFive.reverse()

print("5 Nilai tertinggi adalah: ", topFive)