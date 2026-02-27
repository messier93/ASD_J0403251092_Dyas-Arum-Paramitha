# ============================
# Latihan 2: Tracing Rekursi
# ============================

def countdown(n):
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)

    countdown(n - 1)

    print("Keluar:", n)

countdown(3)

#Mengapa output 'Keluar' muncul terbalik?
#Karena rekursi menggunakan call stack LIFO (last in, first out)
#Saat fungsi countdown(3) dipanggil, program akan berlanjut ke fungsi selanjutnya
#yaitu countdown(2) dan countdown(!) sampai base case n == 0
#Dan setelah base case dicapai, 