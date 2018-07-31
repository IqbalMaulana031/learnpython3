# list (array), dictionary (hashmap, hash array, kv store), tuple, set
daftar_name = ["budi", "andi", "yoga"]
set_name = ("budi", "andi", "yoga")
dict_name = {"budi": "+6234234", "andi": "+62982343", "yoga": "+62323212"}
print(daftar_name, set_name, dict_name)

# list = set (list = mutable, set = immutable)
daftar_name[0] = "andika"
print(daftar_name)
# set_name[0] = "andika"
# print(set_name)
print("panjang daftar_name = {}".format(len(daftar_name)))

for name in daftar_name:
    print(name)

for name in dict_name.keys():
    print("{} = {}".format(name, dict_name[name]))

for name, phone in dict_name.items():
    print(name, phone)

# list
daftar_name.append("nanda")
print(daftar_name)

del daftar_name[0]
print(daftar_name)

dict_name["nanda"] = "+62321"
print(dict_name)

# check if exist `in`

if "nanda" in daftar_name:
    print("nanda dalam daftar nama")

print(type((20,)))
print(type((20, 10)))

a = 5
b = 12

a, b = b, a
print("a = {}, b = {}".format(a, b))
daftar_name.append("budi")
daftar_name.append("budi")
print(daftar_name)
daftar_name_set = set(daftar_name)
print(daftar_name_set)
