# ==========================================================
# Contoh Rekursi 3: Menjumlahkan Elemen List
# ==========================================================

def jumlah_list(data, index=0):
# Base case: jika index sudah mencapai panjang list, kondisi akan berhenti krn tidak ada elemen yg dijumlahkan
    if index == len(data):
        return 0
    
# Recursive case: ambil elemen sekarang ditambah jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1)

#memanggil fungsi dan menampilkan hasil
print(jumlah_list([2, 4, 6, 8])) # Output: 20