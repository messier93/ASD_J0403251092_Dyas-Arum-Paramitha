# ============================
# Contoh Rekursi 1: Faktorial
# =============================

def faktorial(n):
# Base case, kondisi akan berhenti jika n = 0
    if n == 0:
        return 1

# Recursive case: masalah diperkecil menjadi faktorial(n-1) dan fungsi memanggil dirinya sendiri
    return n * faktorial(n - 1)

#Memanggil fungsi dan akan menampilkan hasil
print(faktorial(5)) # Output: 120