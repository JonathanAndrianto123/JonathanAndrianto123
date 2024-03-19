tinggi = int(input("masukkan tinggi = "))
lebar = int(input("masukkan lebar = "))
i = 0
j = 1
l = tinggi * lebar
while i < l :
    print(j, " ", end = "")
    i += 1
    j += 1
    if i % (lebar) == 0 :
        print()

