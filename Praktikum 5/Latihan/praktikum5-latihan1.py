# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2
#===========================
#Latihan 1: Rekursi Pangkat
#===========================
def pangkat (a,n):
    #base case, jika pangkat = 0, hasilnya selalu 1
    if n == 0:
        return 1
    
    #recursive case
    return a * pangkat (a, n-1)

#memanggil fungsi
print(pangkat(2,4)) #output 16

"""
Program pangkat(a, n) menggunakan rekursi untuk 
menghitung nilai aⁿ. Fungsi memeriksa base case 
saat n = 0 dan mengembalikan 1. Jika belum, fungsi 
melakukan recursive call dengan n - 1 lalu mengalikan 
hasilnya dengan a. Proses berulang hingga mencapai base 
case, kemudian hasil dikalikan saat unwinding hingga 
diperoleh aⁿ. Contohnya, pangkat(2,4) menghasilkan 16.
"""
