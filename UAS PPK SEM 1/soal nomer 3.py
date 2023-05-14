#  quiz nomer 3
masukan = list(input("Masukkan Nama: ").split())

for i in range(len(masukan)-1):
    for j in range(len(masukan)-1):
        if masukan[j] > masukan[j+1]:
            par = masukan[j]
            masukan[j] = masukan[j+1]
            masukan[j+1] = par
print("")
for nama in masukan:
    print(nama)




