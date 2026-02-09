# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
#Nama   : Dyas Arum Paramitha
#NIM    : J0403251092
#Kelas  : A2
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
NAMA_FILE = "stok_barang.txt"


# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    """
    Fungsi untuk membaca data stok barang dari file teks
    dan menyimpannya ke dalam dictionary.
    Format data per baris: KodeBarang,NamaBarang,Stok
    """

    stok_dict = {}  # dictionary kosong untuk menampung data stok

    try:
        # Membuka file dalam mode read
        with open(nama_file, "r", encoding="utf-8") as file:
            # Membaca file baris demi baris
            for baris in file:
                baris = baris.strip()  # menghapus karakter newline (\n)

                # Jika baris kosong, lewati
                if baris == "":
                    continue

                # Memecah baris menjadi kode, nama, dan stok
                kode, nama, stok = baris.split(",")

                # Menyimpan data ke dictionary
                stok_dict[kode] = {
                    "nama": nama,
                    "stok": int(stok)
                }

    except FileNotFoundError:
        # Jika file belum ada, program tetap berjalan
        pass

    return stok_dict  # mengembalikan dictionary stok


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Fungsi untuk menyimpan data stok dari dictionary
    ke dalam file teks.
    """

    # Membuka file dalam mode write (menimpa isi lama)
    with open(nama_file, "w", encoding="utf-8") as file:
        # Menulis data secara terurut berdasarkan kode barang
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]   # mengambil nama barang
            stok = stok_dict[kode]["stok"]   # mengambil jumlah stok
            file.write(f"{kode},{nama},{stok}\n")  # menulis ke file


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------
def tampilkan_semua(stok_dict):
    """
    Fungsi untuk menampilkan seluruh data stok barang
    dalam bentuk tabel yang rapi.
    """

    # Jika dictionary kosong
    if len(stok_dict) == 0:
        print("Stok barang kosong.")
        return

    # Header tabel
    print("\n=== DAFTAR STOK BARANG ===")
    print(f"{'KODE':<8} | {'NAMA BARANG':<15} | {'STOK':>5}")
    print("-" * 35)

    # Menampilkan isi data
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"{kode:<8} | {nama:<15} | {stok:>5}")


# -------------------------------
# Fungsi: Cari barang
# -------------------------------
def cari_barang(stok_dict):
    """
    Fungsi untuk mencari barang berdasarkan kode barang.
    """

    kode = input("Masukkan kode barang: ").strip()

    # Mengecek apakah kode ada di dictionary
    if kode in stok_dict:
        print("\n=== BARANG DITEMUKAN ===")
        print("Kode :", kode)
        print("Nama :", stok_dict[kode]["nama"])
        print("Stok :", stok_dict[kode]["stok"])
    else:
        print("Barang tidak ditemukan.")


# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Fungsi untuk menambahkan barang baru ke dalam stok.
    """

    kode = input("Masukkan kode barang baru: ").strip()

    # Validasi kode tidak boleh duplikat
    if kode in stok_dict:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ").strip()

    try:
        # Input stok awal
        stok_awal = int(input("Masukkan stok awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka.")
        return

    # Validasi stok tidak boleh negatif
    if stok_awal < 0:
        print("Stok tidak boleh negatif.")
        return

    # Menyimpan barang baru ke dictionary
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan.")


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    """
    Fungsi untuk mengubah stok barang (tambah / kurangi).
    Stok tidak boleh menjadi negatif.
    """

    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    # Validasi kode barang
    if kode not in stok_dict:
        print("Barang tidak ditemukan.")
        return

    # Menu pilihan update stok
    print("Pilih jenis update:")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try:
        jumlah = int(input("Masukkan jumlah: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka.")
        return

    if jumlah < 0:
        print("Jumlah tidak boleh negatif.")
        return

    # Tambah stok
    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan.")

    # Kurangi stok
    elif pilihan == "2":
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh negatif. Update dibatalkan.")
            return
        stok_dict[kode]["stok"] -= jumlah
        print("Stok berhasil dikurangi.")

    else:
        print("Pilihan tidak valid.")


# -------------------------------
# Program Utama
# -------------------------------
def main():
    """
    Fungsi utama program.
    Menjalankan menu interaktif stok kantin.
    """

    # Membaca data stok saat program dimulai
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
