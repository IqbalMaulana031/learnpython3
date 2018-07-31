print(True)
print(False)
print(type(True))

# operation
print("Not true = {}".format(not True))
print("True == 1", True == 1)
print("False == 0", False == 0)
print("bool(10) = {}".format(bool(10)))

bilangan = 7
if bilangan % 2 == 0:
    print("genap")
else:
    print("ganjil")

if 5 < bilangan < 10:
    print("bilangan antara 5 dan 10")
a = "test"
b = "test"
print(""" "a" != "b" = {}""".format(a != b))

if bilangan >= 7:
    print("bilangan lebih dari atau sama dengan 7")

# is operator
# is -> is two object point to the same object
# == -> is two object have the same value
daftar_nilai = [1, 2, 3]
copy_daftar_nilai = daftar_nilai
print(
    "copy_daftar_nilai is daftar_nilai = {}".format(copy_daftar_nilai is daftar_nilai)
)

# None value
print("None == None = {}".format(None == None))
print("None is None = {}".format(None is None))
