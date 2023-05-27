# sudut = float(input())
# if sudut < 90:
#     print("Sudut lancip")
# elif sudut == 90:
#     print("Sudut siku-siku")
# elif sudut > 90 and sudut < 180:
#     print("Sudut tumpul")
# else:
#     print("Sudut lurus")

# latihan nomer 1
# masukan=int(input("masukkan sebuah tahun: "))
# if masukan%100==0:
#     if masukan%400==0:
#         print(masukan,"adalah tahun kabisat")
#     else:
#         print(masukan,"bukan tahun kabisat")
# elif masukan%4==0:
#     print(masukan, "adalah tahun kabisat")
# else:
#     print(masukan, "bukan tahun kabisat")
    
# masukan=int(input("masukkan sebuah tahun: "))
# if masukan%400==0:
#     print(masukan,"tahun kabisat")
# elif masukan%4==0:
#     if masukan%100==0:
#         print(masukan, "bukan tahun kabisat")
#     else:
#         print(masukan, "tahun kabisat")

    
    
# latihan nmr 2
# masukan= int(input("masukkan tahun: "))
# if masukan%400==0 or (masukan%4==0 and masukan%100!=0):
#     print(masukan,"adalah tahun kabisat")
# else:
#     print(masukan,"bukan tahun kabisat")

# # latihan nmr 3
# masukan=list(map(int,input("masukkan 3 bilangan berbeda (dengan spasi): ").split()))
# if(masukan[0]>masukan[1] and masukan[0]>masukan[2]):
#     print(masukan[0],"adalah bilangan terbesar")
# elif(masukan[1]>masukan[0] and masukan[1]>masukan[2]):
#     print(masukan[1],"adalah bilangan terbesar")
# elif(masukan[2]>masukan[1] and masukan[2]>masukan[0]):
#     print(masukan[2],"adalah bilangan terbesar")
# else:
#     print("mohon masukkan angka yang benar")

# # latihan 3
# x,y,z=list(map(int,input().split()))    
# if x>y and x>z:
#     print(x)
# elif y>x and y>z:
#     print(y)
# elif z>x and z>y:
#     print(z)
    
# # quiz 1
# masukan=float(input())
# masukan1 = int(masukan)
# masukan2 = float(masukan1+0.4)
# if(masukan >= masukan2):
#     print(masukan1+1)
# else:
#     print(masukan1)
    
# # quiz 2
# x=list(map(int,input().split()))
# if x[0]>x[1]>x[2] or x[2]>x[1]>x[0]:
#     print(x[1])
# elif x[1]>x[0]>x[2] or x[2]>x[0]>x[1]:
#     print(x[0])
# elif x[0]>x[2]>x[1] or x[1]>x[2]>x[0]:
#     print(x[2])
# else:
#     print("masukkan bil yang benar")

# quiz 3
tanggal,bulan,tahun=list(map(int,input("masukkan tgl bln thn: ").split()))
if (tahun%400==0 or (tahun%4==0 and tahun%100!=0)):
    if bulan>=1 and bulan<=12:
            if bulan>=1 and bulan<=7:
                if bulan==2:
                    if tanggal>=1 and tanggal<=29:
                        print("valid")
                    else:
                        print("tidak valid")
                elif bulan%2==1:
                    if tanggal>=1 and tanggal<=31:
                        print("valid")
                    else:
                        print("tidak valid")
                elif bulan%2==0:
                    if tanggal>=1 and tanggal<=30:
                        print("valid")
                    else:
                        print("tidak valid")
            elif bulan>=8 and bulan<=12:
                if bulan%2==0:
                    if tanggal>=1 and tanggal<=31:
                        print("valid")
                    else:
                        print("tidak valid")
                elif bulan%2==1:
                    if tanggal>=1 and tanggal<=30:
                        print("valid")
                    else:
                        print("tidak valid")
    else:
        print("tidak valid")
else:
    if bulan>=1 and bulan<=12:
            if bulan>=1 and bulan<=7:
                if bulan==2:
                    if tanggal>=1 and tanggal<=28:
                        print("valid")
                    else:
                        print("tidak valid")
                elif bulan%2==1:
                    if tanggal>=1 and tanggal<=31:
                        print("valid")
                    else:
                        print("tidak valid")
                elif bulan%2==0:
                    if tanggal>=1 and tanggal<=30:
                        print("valid")
                    else:
                        print("tidak valid")
            elif bulan>=8 and bulan<=12:
                if bulan%2==0:
                    if tanggal>=1 and tanggal<=31:
                        print("valid")
                    else:
                        print("tidak valid")
                elif bulan%2==1:
                    if tanggal>=1 and tanggal<=30:
                        print("valid")
                    else:
                        print("tidak valid")
    else:
        print("tidak valid")







