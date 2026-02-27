# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2
# =================================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
# =================================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:
        return
    
    # Base case, jika panjang string sudah , maka cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Pilih '0' tidak menambah jumlah_!
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih '1' menambah jumlah_! sebanyak 1
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

#memanggil fungsi
biner_batas(4, 2)
