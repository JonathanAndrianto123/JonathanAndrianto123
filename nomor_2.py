def baris(n):
    for i in range(n, 0, -1):
        print(str(faktor(i)) + " ", end="")
        for j in range(i, 0, -1):
            print(str(j) + " ", end="")
        print()

def faktor(bil):
    if bil == 1 or bil == 0:
        return 1
    return bil * faktor(bil - 1)

n = int(input("Masukkan n = "))
baris(n)

