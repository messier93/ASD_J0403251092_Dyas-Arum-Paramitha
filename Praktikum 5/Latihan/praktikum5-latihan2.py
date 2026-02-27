# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2
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

""" Mengapa output 'Keluar' muncul terbalik?
Karena rekursi menggunakan call stack LIFO (last in, first out) 
saat fungsi countdown(3) dipanggil, program akan berlanjut ke fungsi 
selanjutnya yaitu countdown(2) dan countdown(1) sampai base case n == 0.
Setelah base case dicapai, proses akan kembali jalan ke fungsi sebelumnya. 
Dan karena fungsi yang terakhir dipanggil adalah yang pertama selesai, maka 
urutan  print bagian keluar menjadi terbalik
dari urutan masuknya """"

