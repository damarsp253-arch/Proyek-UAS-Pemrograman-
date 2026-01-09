class MahasiswaView:
    def tampilkan_data(self, data):
        print("\n=== DAFTAR NILAI MAHASISWA ===")
        print("-" * 45)
        print(f"{'No':<5}{'Nama':<15}{'NIM':<15}{'Nilai'}")
        print("-" * 45)

        for i, mhs in enumerate(data, start=1):
            print(f"{i:<5}{mhs.nama:<15}{mhs.nim:<15}{mhs.nilai}")

        print("-" * 45)
