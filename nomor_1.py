def prima(bilangan) :
    if bilangan <= 1 :
        return False
    for i in range (2, int(bilangan ** 0.5) + 1) :
        if bilangan % i == 0 :
            return False
        else :
            return True
        
def primaterdekat(bil2) :
    for i in range (bil2 - 1, 1, -1) :
        if prima(i) :
            return i
        
bil2 = int(input("Masukkan bilangan = "))
hasil = primaterdekat(bil2)
print(f"Bilangan prima terdekat dari {bil2} adalah {hasil}")

