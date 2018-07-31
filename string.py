name = "budi"
name2 = "andi"

print(name[0])
print(name2[0])
print("panjang dari name = {}".format(len(name)))
print("panjang dari name2 = {}".format(len(name2)))

# name3 = input("name 3 = ")
name3 = "yoga"
print("name3 = {}".format(name3))
print("value1", name, name2, name3)
print("value1", name, name2, name3, sep="|")
print("value1", name, name2, name3, end=".\n")

# alternative 1
output_file = open("output.txt", "w+")
print(name, name2, name3, file=output_file, flush=True)
output_file.close()

# alternative 2
with open("output.txt", "w+") as output_file:
    print(name, name2, name3, file=output_file, flush=True)

#                             0     1
print("{1} {0} {1}".format("one", "two"))  # two one two

print("{0!s} {0!r}".format(10 / 3))
print("{:>10}".format(name2))
print("{:10}".format(name2))
