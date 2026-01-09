
# ===== CLASS DATA =====
class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai


# ===== CLASS PROCESS =====
class MahasiswaProcess:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah_mahasiswa(self, nama, nim, nilai):
        # Validasi input
        if nama == "" or nim == "":
            raise ValueError("Nama dan NIM tidak boleh kosong")

        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus antara 0 sampai 100")

        mahasiswa = Mahasiswa(nama, nim, nilai)
        self.data_mahasiswa.append(mahasiswa)

    def get_data(self):
        return self.data_mahasiswa


# ===== CLASS VIEW =====
class MahasiswaView:
    def tampilkan_data(self, data):
        print("\n=== DAFTAR NILAI MAHASISWA ===")
        print("-" * 45)
        print(f"{'No':<5}{'Nama':<15}{'NIM':<15}{'Nilai'}")
        print("-" * 45)

        for i, mhs in enumerate(data, start=1):
            print(f"{i:<5}{mhs.nama:<15}{mhs.nim:<15}{mhs.nilai}")

        print("-" * 45)


# ===== PROGRAM UTAMA =====
def main():
    proses = MahasiswaProcess()
    view = MahasiswaView()

    while True:
        print("\nMENU PROGRAM")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        try:
            if pilihan == "1":
                nama = input("Masukkan Nama   : ")
                nim = input("Masukkan NIM    : ")
                nilai = int(input("Masukkan Nilai  : "))

                proses.tambah_mahasiswa(nama, nim, nilai)
                print("Data berhasil ditambahkan!")

            elif pilihan == "2":
                data = proses.get_data()
                if len(data) == 0:
                    print("Belum ada data mahasiswa.")
                else:
                    view.tampilkan_data(data)

            elif pilihan == "3":
                print("Program selesai. Terima kasih.")
                break

            else:
                print("Menu tidak tersedia!")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Terjadi kesalahan input!")

if __name__ == "__main__":
    main()
