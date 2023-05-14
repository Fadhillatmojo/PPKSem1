# soal nomer 2

# gambar pertama
for baris in range(5):
    if baris % 2 == 0:
        for i in range(12):
            if i == 0:
                print("x",end="")
            elif i == 11:
                print("x")
            else:
                print("-",end="")
    else:
        if baris == 1:
            for k in range(2):
                print("|")
        else:
            for m in range(2):
                for l in range(12):
                    if l == 0:
                        print("|",end="")
                    elif l>0 and l<11:
                        print(" ",end="")
                    else:
                        print("|")

print("") 

# gambar 2
for baris in range(5):
    if baris % 2 == 0:
        for i in range(12):
            if i == 0:
                print("x",end="")
            elif i == 11:
                print("x")
            elif 0<i<11 and baris != 4:
                print("-",end="")
            else:
                print(" ",end="")

    else:
        for m in range(2):
                for l in range(12):
                    if l == 0:
                        print("|",end="")
                    elif l>0 and l<11:
                        print(" ",end="")
                    else:
                        print("|")
