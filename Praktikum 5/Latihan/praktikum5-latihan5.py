# Nama  : Dyas Arum Paramitha
# NIM   : J0403251092
# Kelas : TPL A2

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    #base case,  jika panjang PIN sudah sesuai  maka cetak hasil
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    #loop untuk setiap kemungkinan angka yaitu 0,1,2
    for angka in ["0", "1", "2"]:
        #recursive call tambahkan angka saat ini ke hasil
        buat_pin(panjang, hasil + angka)

#memanggil fungsi utk menghasilkan pin 3 digit
buat_pin(3)

"""
Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?
Program saat ini menghasilkan semua kombinasi PIN 3 digit dari angka 0–2, 
termasuk angka yang sama berulang. Untuk mencegah angka berulang, sebelum 
melakukan recursive call bisa dicek: jika angka yang akan ditambahkan sama 
dengan angka terakhir di hasil, lewati.
"""
