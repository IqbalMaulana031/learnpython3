# if, for, while, break, continue

if True:
    print("benar")

nilai = 70
if nilai >= 65:
    print("lulus")
elif nilai >= 50:
    print("hampir lulus")
else:
    print("tidak lulus")

for i in range(100):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

# force break on i == 50
for i in range(100):
    if i == 50:
        break
    print(i)

# skip even number
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)
