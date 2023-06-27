# kelompok 9

jml=int(input())
ipk=0
totalSks = 0

for i in range(jml):
    x=input().split()
    sks=int(x[1])
    nilai = x[2]
    newNilai = 0
    if nilai == "A":
        newNilai = 4
    elif nilai == "B":
        newNilai = 3
    elif nilai == "C":
        newNilai = 2
    elif nilai == "D":
        newNilai = 1
    elif nilai == "E":
        newNilai = 0
    ipk = ipk + (sks*newNilai)
    totalSks = totalSks + sks

newIpk=ipk/totalSks
print("{:.2f}".format(newIpk))


    