from model.daftar_nilai import *


def cetak_daftar_nilai():
    if x.items():
        print("=" * 78)
        print("|                               Daftar Mahasiswa                             |")
        print("=" * 78)
        print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("=" * 78)
        i = 0
        for z in x.items():
            i += 1
            print("| {no:2d} | {0:15s} | {1:15s} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                  .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
        print("=" * 78)
    else:
        print("=" * 78)
        print("|                               Daftar Mahasiswa                             |")
        print("=" * 78)
        print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("=" * 78)
        print("|                                TIDAK ADA DATA                              |")
        print("=" * 78)


def cetak_hasil_pencarian():
    nama = input("Masukkan Nama        : ")
    if nama in x.keys():
        print("=" * 73)
        print("|                             Daftar Mahasiswa                          |")
        print("=" * 73)
        print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("=" * 73)
        print("| {0:15s} | {1:15s} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
              .format(nama, x[nama][0], x[nama][1], x[nama][2], x[nama][3], x[nama][4]))
        print("=" * 73)
