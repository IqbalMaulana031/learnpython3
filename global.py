nilai = 60


def set_nilai(new_nilai):
    nilai = new_nilai
    print(nilai)


def set_nilai_global(new_nilai):
    global nilai
    nilai = new_nilai
    print(nilai)


# set_nilai(20)
set_nilai_global(20)
print(nilai)
