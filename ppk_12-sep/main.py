# #praktik
# listAwal=input("masukkan jari alas dan tinggi: ").split()
# listAwalNew=list(map(float,listAwal))
# tinggi=listAwalNew[1]
# jari=listAwalNew[0]
# luasPermukaan=3.14*jari*jari*2+(2*3.14*jari*tinggi)
# print("LP nya adalah: ",luasPermukaan)

# #latihan 1
# masukanBaris1=input("masukkan 2 angka berspasi: ")
# masukanBaris2=input("masukkan 2 angka berspasi: ")
# newBaris1=list(map(int,masukanBaris1.split()))
# newBaris2=list(map(int,masukanBaris2.split()))
# print(newBaris1[0]+newBaris1[1]+newBaris2[0]+newBaris2[1])
    
#quiz 1
print("masukkan 2 angka dengan spasi")
firstMatriks1=input().split()
firstMatriks2=input().split()
print("")
secondMatriks1=input().split()
secondMatriks2=input().split()

firstMatriks1=list(map(int,firstMatriks1))
firstMatriks2=list(map(int,firstMatriks2))
secondMatriks1=list(map(int,secondMatriks1))
secondMatriks2=list(map(int,secondMatriks2))

hasil1=firstMatriks1[0]*secondMatriks1[0]+firstMatriks1[1]*secondMatriks2[0]
hasil2=firstMatriks1[0]*secondMatriks1[1]+firstMatriks1[1]*secondMatriks2[1]
hasil3=firstMatriks2[0]*secondMatriks1[0]+firstMatriks2[1]*secondMatriks2[0]
hasil4=firstMatriks2[0]*secondMatriks1[1]+firstMatriks2[1]*secondMatriks2[1]

print(hasil1,hasil2)
print(hasil3,hasil4)

#quiz 1
print("masukkan 2 angka dengan spasi")
firstMatriks1=list(map(int,input().split()))
firstMatriks2=list(map(int,input().split()))
secondMatriks1=list(map(int,input().split()))
secondMatriks2=list(map(int,input().split()))

hasil1=firstMatriks1[0]*secondMatriks1[0]+firstMatriks1[1]*secondMatriks2[0]
hasil2=firstMatriks1[0]*secondMatriks1[1]+firstMatriks1[1]*secondMatriks2[1]
hasil3=firstMatriks2[0]*secondMatriks1[0]+firstMatriks2[1]*secondMatriks2[0]
hasil4=firstMatriks2[0]*secondMatriks1[1]+firstMatriks2[1]*secondMatriks2[1]
print("")
print(hasil1,hasil2)
print(hasil3,hasil4)



