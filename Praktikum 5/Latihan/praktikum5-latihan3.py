# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2
# ==================================
# Latihan 3: Mencari Nilai Maksimum
# ==================================

def cari_maks(data, index=0):
    # Base case, jika index sudah di elemen terakhir maka 
    # kembalikan nilai elemen tsb
    if index == len(data) - 1:
        return data[index]
    
    # Recursive case, mencari maksimum dari sisa elemen
    # setelah index sekarang
    maks_sisa = cari_maks(data, index + 1)
    
    # Bandingkan elemen sekarang dengan max dari sisa elemen 
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa

angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

"""
Program bekerja dengan membandingkan setiap elemen 
dengan nilai maksimum sisa elemen. Proses dimulai dari 
index 0 dan memanggil fungsi dengan index + 1 hingga 
mencapai elemen terakhir. Base case terjadi saat 
index == len(data) - 1, di mana fungsi langsung 
mengembalikan nilai elemen terakhir. Setelah itu, 
setiap pemanggilan membandingkan elemen saat ini 
dengan maksimum dari sisa elemen (maks_sisa) dan 
mengembalikan yang lebih besar ke panggilan sebelumnya, 
sehingga akhirnya diperoleh nilai maksimum seluruh list.
"""
