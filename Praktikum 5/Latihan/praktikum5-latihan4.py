# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):
    # Base case:
    # Jika panjang string sudah sama dengan n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # Pilih 'A' dan lanjutkan rekursi
    kombinasi(n, hasil + "A")
    
    # Pilih 'B' dan lanjutkan rekursi
    kombinasi(n, hasil + "B")

# Memanggil fungsi untuk kombinasi panjang 2
kombinasi(2)

"""
Program kombinasi(n) menghasilkan semua kemungkinan
kombinasi huruf A dan B sepanjang n menggunakan rekursi 
backtracking. Fungsi memeriksa base case saat panjang 
string = n dan mencetak kombinasi. Jika belum tercapai,
ungsi menambahkan huruf A atau B di setiap posisi 
melalui recursive call. Karena setiap posisi
memiliki 2 kemungkinan, jumlah kombinasi yang dihasilkan 
adalah 2ⁿ. Misalnya, untuk n = 2, kombinasi yang 
dihasilkan adalah AA, AB, BA, dan BB
"""
