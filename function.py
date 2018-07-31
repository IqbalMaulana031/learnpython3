def nama_function(name, job):
    print("Hi {}, your job is {}".format(name, job))

def tambah(a, b):
    """tambah untuk menambahkan dua bilangan a dan b"""
    return a + b

kali = lambda x,y : x * y


nama_function("Budi", "Security Consultant")
print("tambah(2,5) = {}".format(tambah(2,5)))
print(tambah.__doc__)
print("kali(2,5) = {}".format(kali(2,5)))