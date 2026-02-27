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
Program kombinasi(n) menghasilkan semua kemungkinan kombinasi 
huruf A dan B dengan panjang n menggunakan rekursi backtracking. 
Alur program dimulai dengan memeriksa base case, yaitu saat panjang 
string = n, maka kombinasi dicetak dan rekursi berhenti. 
Jika base case belum tercapai, program masuk ke recursive call, di mana 
setiap posisi menambahkan huruf A atau B dan memanggil fungsi kembali untuk 
posisi berikutnya. Karena setiap posisi memiliki 2 kemungkinan, maka jumlah 
kombinasi yang dihasilkan adalah 2 pangkat n (2ⁿ). Misalnya, untuk n = 2, 
jumlah kombinasi adalah 2² = 4, yaitu AA, AB, BA, dan BB.
"""