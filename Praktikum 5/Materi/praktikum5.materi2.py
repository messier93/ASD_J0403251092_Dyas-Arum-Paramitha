# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2
# =======================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
# =======================================

def hitung(n):
# Base case, kondisi akan berhenti jika n = 0
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n) # fase stacking (sebelum rekursi dipanggil)
    hitung(n - 1) # pemanggilan rekursif 
    print("Keluar:", n) # fase unwinding

#memanggil fungsi

hitung(3)
