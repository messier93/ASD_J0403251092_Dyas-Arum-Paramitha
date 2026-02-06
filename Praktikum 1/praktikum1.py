#================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#================================================

print("---Membuka file dalam satu string---")
with open("dataMahasiswa.txt","r",encoding="utf-8") as file:
    isiFile = file.read()
print(isiFile)

print("Tipe Data :", type(isiFile))

print("---Membuka file per barisssssssssssss---")
jumlahBaris = 0
with open("dataMahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file :
        jumlahBaris = jumlahBaris + 1
        baris = baris
        print("baris ke-", jumlahBaris)
        print("isinya :", baris)

#======================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 2 : Membaca data dan menyimpannya ke struktur data list
#======================================================================
#Parsing baris menjadi data satuan dan menampilkannya didalam bentuk kolom data
with open ("dataMahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai)

#==========================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 3 : Membaca data dan menyimpannya dalam list
#==========================================================
#Membaca seluruh isi 
dataList = []
with open ("dataMahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        dataList.append([nim, nama, int(nilai)]) #menyimpan data ke list
print("---Show List---")
print(dataList)
print("Contoh record ke 1: ", dataList[0])
print("Contoh record ke 2: ", dataList[1])
print("Jumlah record", len(dataList))

#================================================================
#Praktikum 1 : Konsep ADT dan FIle Handling
#Latihan Dasar 4 : Membaca data dan menyimpannya dalam dictionary
#================================================================
#Membaca data dan menyimpannya ke struktur data dictionary
dataDict = {} #inisialisasi dict
with open ("dataMahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter garis baru
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan dan simpan ke variabel
        #simpan data di dict
        dataDict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai),
        }
print("---Show Dictionary---")
print(dataDict)