# # latihan 1
# masukan = int(input())
# arrayHari = ["senin","selasa", "Rabu", "Kamis", "Jumat", "Jumat", "sabtu", "minggu","minggu", "minggu" ]
# for i in range(0, len(arrayHari)):
#     if i == masukan % 10:
#         print(arrayHari[i-1])
        
# latihan 2
c = int(input())
array = list(range(c))
for a in range(c):
    for b in array:
        if (a**2 + b**2 == c**2):
            print(a,b)

# # quiz 1
# n = int(input())
# tipe = True
# if n == 0 or n == 1:
#     tipe = False
# for i in range(2,n):
#     if n % i == 0:
#         tipe = False
# if tipe == True:
#     print("PRIMA")
# else:
#     print("BUKAN PRIMA")
    
# # quiz 2
# masukan = int(input())
# for i in range(masukan):
#     for i in range(masukan):
#         print("#", end="")
#     print("")   

# # quiz 3
# masukan = int(input())
# for i in range(masukan):
#     if i > 0 and i < masukan-1:
#         print("#",end="")
#         for i in range(masukan-2):
#             print(" ",end="")
#         print("#", end="")
#     else:
#         for i in range(masukan):
#             print("#", end="")
#     print("")
    











