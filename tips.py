# learn Zen of Python
import this

print("=" * 80)

# format string
nilai = 10

print(f"nilai = {nilai}")

score = "good" if nilai > 75 else "bad"
print(f"score = {score}")

title = "Reverse a string"
title_reverse = title[::-1]
print(f"reverse string = {title_reverse}")

# get memory usage of object
import sys

print("size of reverse string = {} bytes".format(sys.getsizeof(title_reverse)))

# extended unpacking

first, *middle, last = "my name"
print(first)
print(middle)
print(last)


# joining list

names = ["budi", "yoga", "andi", "ali"]
print(", ".join(names))


# disassembly python code
def add(a, b):
    return a + b


import dis

dis.dis(add)
