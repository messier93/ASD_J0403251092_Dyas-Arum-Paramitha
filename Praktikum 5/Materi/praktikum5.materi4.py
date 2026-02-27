# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2
# ============================================
# Contoh Backtracking 1: Kombinasi Biner (n)
# ============================================

def biner(n, hasil=""):
    # Base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + Explore: tambah '0' ke string dan lanjutkan rekursi
    biner(n, hasil + "0")

    # Choose + Explore: tambah '1' ke string dan lanjutkan rekursi
    biner(n, hasil + "1")

# Memanggil fungsi
biner(3)
