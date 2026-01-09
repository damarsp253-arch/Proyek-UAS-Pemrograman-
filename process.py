from data import Mahasiswa

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

    def tampilkan_mahasiswa(self):
        return self.data_mahasiswa
