daftarBuronan = []

def tampilanMenu():
    print("===== Sistem pendataan buronan =====")
    print("1. Tambah data buronan")
    print("2. Tampilkan data buronan")
    print("3. Ubah Data Buronan")
    print("4. Hapus Data Buronan")
    print("5. Selesai")
    print("=====================================")

def Iangka(t):
    while True:
        nilai = input(t)
        if nilai.isdigit():
            return int(nilai)
        else:
            print("Input harus berupa angka")

def Databuronan():
    print("\n==== Tambah data buronan =====")
    nama = input("Nama tersangka   : ")
    while nama == "":
        print("Nama tidak boleh kosong!")
        nama = input("Nama tersangka   : ")

    jenis = input("Jenis kejahatan  : ")
    while jenis == "":
        print("Jenis kejahatan tidak boleh kosong")
        jenis = input("Jenis kejahatan  : ")

    bahaya = Iangka("Tingkat bahaya (1-10): ")
    while not (1 <= bahaya <= 10):
        print("Tingkat bahaya harus di antara 1 sampai 10!")
        bahaya = Iangka("Tingkat bahaya (1-10): ")

    daftarBuronan.append((nama, jenis, bahaya))
    print("Data '" + nama + "' berhasil ditambahkan.")

def tampilburonan():
    print("\n==== Daftar buronan =====")
    if len(daftarBuronan) == 0:
        print("Belum ada data buronan yang tercatat")
        return
    print("No".ljust(4) + "Nama Tersangka".ljust(25) + "Jenis Kejahatan".ljust(25) + "Tingkat Bahaya".ljust(25))

    no = 1
    for buronan in daftarBuronan:
        nama = buronan[0]
        jenis = buronan[1]
        bahaya = buronan[2]
        print(str(no).ljust(4) + nama.ljust(25) + jenis.ljust(25) + str(bahaya))
        no += 1

def Data2():
    tampilburonan()
    if len(daftarBuronan) == 0:
        return None

    while True:
        index = Iangka("Masukkan nomor data yang ingin diubah: ") - 1
        if 0 <= index < len(daftarBuronan):
            return index
        else:
            print("Nomor data tidak valid")

def ubahData():
    print("====== Ubah data buronan ======")
    index = Data2()
    if index is None:
        print("Proses ubah data dibatalkan.")
        return

    namasebelum = daftarBuronan[index][0]
    jenissebelum = daftarBuronan[index][1]
    bahayasebelum = daftarBuronan[index][2]
    print("Data lama: " + namasebelum + ", " + jenissebelum + ", " + str(bahayasebelum))

    namasekarang = input("Nama buronan baru [" + namasebelum + "]: ")
    if namasekarang == "":
        namasekarang = namasebelum

    jenissekarang = input("Jenis kejahatan baru [" + jenissebelum + "]: ")
    if jenissekarang == "":
        jenissekarang = jenissebelum

    changebahaya = input("Ubah tingkat bahaya? (y/n) [" + str(bahayasebelum) + "]: ")
    if changebahaya == "y":
        bahayasekarang = Iangka("Tingkat bahaya baru (1-10): ")
        while not (1 <= bahayasekarang <= 10):
            print("Tingkat bahaya harus di antara 1 sampai 10")
            bahayasekarang = Iangka("Tingkat bahaya baru (1-10): ")
    else:
        bahayasekarang = bahayasebelum
    daftarBuronan[index] = (namasekarang, jenissekarang, bahayasekarang)
    print("Data berhasil diubah.")

def hapusdata():
    print("==== Hapus data buronan ====")
    print("Gunakan menu ini jika buronan tidak bersalah / kasus diberhentikan")
    index = Data2()
    if index is None:
        print("Proses hapus data dibatalkan.")
        return

    nama = daftarBuronan[index][0]
    print("Alasan penghapusan data '" + nama + "':")
    print("1. Buronan tidak bersalah")
    print("2. Kasus diberhentikan")

    alasan = input("Pilih alasan (1/2): ")
    while alasan != "1" and alasan != "2":
        print("Pilihan tidak ada! Masukkan 1 atau 2.")
        alasan = input("Pilih alasan (1/2): ")

    if alasan == "1":
        keterangan = "buronan tidak bersalah"
    else:
        keterangan = "kasus diberhentikan"

    konfirmasi = input("Yakin ingin menghapus data " + nama + "' (" + keterangan + ")? (y/n): ")
    if konfirmasi == "y":
        daftarBuronan.pop(index)
        print("Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

def main():
    while True:
        tampilanMenu()
        pilihan = input("Pilih menu (1-5): ")
        if not pilihan.isdigit():
            print("Input tidak valid! Masukkan angka 1-5.")
            continue
        pilihan = int(pilihan)

        if pilihan == 1:
            Databuronan()
        elif pilihan == 2:
            tampilburonan()
        elif pilihan == 3:
            ubahData()
        elif pilihan == 4:
            hapusdata()
        elif pilihan == 5:
            print("Data catatan buronan kepolisian selesai...")
            break
        else:
            print("Pilihan tidak ada selain angka (1-5)")
main()