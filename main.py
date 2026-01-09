from process import MahasiswaProcess
from view import MahasiswaView

def main():
    proses = MahasiswaProcess()
    view = MahasiswaView()

    mahasiswa = None
    while mahasiswa is None:
        mahasiswa = proses.input_mahasiswa()

    view.tampilkan_data(mahasiswa)

if __name__ == "__main__":
    main()
    