def print_list_nilai(*nilai, jumlah_siswa=20, **kwargs):
    print(nilai)
    print(kwargs)
    if "guru" in kwargs and kwargs["guru"] == "budi":
        print("confirm ke pak budi")
    print("jumlah siswa = {}".format(jumlah_siswa))


print_list_nilai(10, 20, 30, mata_pelajaran="math", guru="budi")
print("=" * 100)
print_list_nilai(10, 20, 30, jumlah_siswa=40)


def handleIOError(e):
    print("do something with IO error")


try:
    file = open("test2.txt", "r")
    file.read(10)
    nilai = 10 / 0
except IOError as e:
    handleIOError(e)
except ZeroDivisionError as e:
    print(e)
