# --- Praktikum 2: Konsep ADT dan File Handling (Case Study) ---
# --- Latihan 1  : Membuay fungsi load data dari file ---

#variabel menyimpan data file
namaFile = "dataMahasiswa.txt"

def bacaData(namaFile):
    dataDict = {} #inisialisasi data dict
    with open(namaFile,"r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") # ambil data per item data
            dataDict[nim] = {"nama": nama, "nilai": int(nilai)}
    return dataDict

bukaData = bacaData(namaFile) #memanggil fungsi load data dan menyimpan dalam
print("Jumlah data terbaca", len(bukaData))

# --- Praktikum 2: Konsep ADT dan File Handling (Case Study) ---
# --- Latihan 2  : Membuay fungsi load data dari file ---

def tampilkanData(dataDict):
    #Membuat header table
    print("\n--- DAFTAR MAHASISWA ---")
    print(f"{'NIM' : <10} | {'NAMA': <12} | {'NILAI' : >5}")

    '''
    Untuk tampilan yg rapi harus atur lebar kolom
    nim <10 brrti nim rata kiri dgn lebar kolom 12 char
    nilai <5 brti nilai rata kananan dengan lebar 5 char
    '''
    print("-"*40) #membuat garis

    #menampilkan isi datanya
    for nim in sorted(dataDict.keys()):
        nama = dataDict[nim]["nama"]
        nilai = dataDict[nim]["nilai"]
        print(f"{nim : <10} | {nama: <12} | {nilai : >5}")

# data akan ditampilkan melalui menu interaktif

# --- Praktikum 2: Konsep ADT dan File Handling (Case Study) ---
# --- Latihan 3  : Membuat fungsi mencari data

#membuat fungsi pencarian data
def cariData(dataDict):
    #pencarian data berdasarkan nim sbg key dict
    #membuat input nim mhsw yang akan dicari
    cariNim =  input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if cariNim in dataDict:
        nama = dataDict[cariNim]["nama"]
        nilai = dataDict[cariNim]["nilai"]

        print("--- Data Mahasiswa Ditemukan ---")
        print(f"NIM: {cariNim}")
        print(f"Nama: {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("--- Data mahasiswa tidak ditemukan. Pastikan data yang dimasukkan benar. ---")

# pencarian akan dipanggil melalui menu

# --- Praktikum 2: Konsep ADT dan File Handling (Case Study) ---
# --- Latihan 4  : Membuat function update data ---
def ubahData(dataDict):
    # awali dengan mencari nim/data mahasiswa
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in dataDict:
        print("NIM tidak ditemukan. Update gagal.")
        return

    try:
        nilaiBaru = int(input("Masukkan nilai yang baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka.")
        return

    if nilaiBaru < 0 or nilaiBaru > 100:
        print("Nilai harus antara 0 sampai 100.")
        return

    nilaiLama = dataDict[nim]["nilai"]
    dataDict[nim]["nilai"] = nilaiBaru

    print(f"Update berhasil. NIM {nim} nilai berubah dari {nilaiLama} menjadi {nilaiBaru}")

# ubah data dipanggil melalui menu

# --- Praktikum 2: Konsep ADT dan File Handling (Case Study) ---
# --- Latihan 5  : Membuat function menyimpan data pada file ---

#fungsi save data ke file
def simpanData(namaFile, dataDict):
    with open(namaFile,"w",encoding="utf-8") as file:
        for nim in sorted(dataDict.keys()):
            nama = dataDict[nim]["nama"]
            nilai = dataDict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# penyimpanan dipanggil melalui menu

# --- Praktikum 2: Konsep ADT dan File Handling (Case Study) ---
# --- Latihan 6  : Membuat menu interaktif ---

def main():
    while True:
        print("\n--- MENU DATA ---")
        print("1. Tampilkan data mahasiswa.")
        print("2. Cari data berdasarkan NIM.")
        print("3. Ubah nilai mahasiswa.")
        print("4. Simpan data ke file.")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-4): ").strip()

        if pilihan == '1':
            tampilkanData(bukaData)
        elif pilihan == '2':
            cariData(bukaData)
        elif pilihan == '3':
            ubahData(bukaData)
        elif pilihan == '4':
            simpanData(namaFile, bukaData)
            print("Data berhasil disimpan.")
        elif pilihan == '0':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()