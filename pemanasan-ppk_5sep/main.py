# soal nomer 1
r= int(input("masukkan jari jari:"))
t=int(input("masukkan tinggi:"))
pi=3.14
l=2*pi*r*(r+t)
print(l)

#soal nomer 2
n= int(input("masukkan angka:"))

if(n>=100 and n<=999):
    x=n%100
    y=x/10
    print("digit tengah:"+ str(int(y)))
else:
    print("angka tidak dalam range")

#soal nomer 3
txt=input("masukkan angka antara 100-999:")
print(txt[1])
    