from view.input_nilai import *

x = {}


def tambah_data():
    global x
    nama = input_nama()
    nim = input_nim()
    uts = input_uts()
    uas = input_uas()
    tugas = input_tugas()
    akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
    x[nama] = nim, tugas, uts, uas, akhir
    return x


def ubah_data():
    nama = input("Masukkan Nama: ")
    if nama in x.keys():
        nim = input_nim()
        uts = input_uts()
        uas = input_uas()
        tugas = input_tugas()
        akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
        x[nama] = nim, tugas, uts, uas, akhir
    else:
        print("Nama {0} tidak ditemukan".format(nama))


def hapus_data():
    nama = input("Masukkan Nama:  ")
    if nama in x.keys():
        del x[nama]
    else:
        print("Nama {0} Tidak Ditemukan".format(nama))


def cari_data():
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
