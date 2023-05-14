# quiz nomer 4

a, b=list(map(int,input().split()))
c, d=list(map(int,input().split()))
e, f=list(map(int,input().split()))
g, h=list(map(int,input().split()))

hasil1 = a*e + b*g
hasil2 = c*e + d*g
hasil3 = a*f + b*h
hasil4 = c*f + d*h

print(hasil1,hasil3)
print(hasil2,hasil4)

# alternatif lain

arrayMatriks = []
arrayHasilMatriks = []
for i in range(4):
    x = input().split()
    arrayMatriks.append(x)
for i in arrayMatriks:
    for j in range(2):
        i[j] = int(i[j])
print("")
hasil1 = arrayMatriks[0][0]*arrayMatriks[2][0] + arrayMatriks[0][1]*arrayMatriks[3][0]
hasil2 = arrayMatriks[1][0]*arrayMatriks[2][0] + arrayMatriks[1][1]*arrayMatriks[3][0]
hasil3 = arrayMatriks[0][0]*arrayMatriks[2][1] + arrayMatriks[0][1]*arrayMatriks[3][1]
hasil4 = arrayMatriks[1][0]*arrayMatriks[2][1] + arrayMatriks[1][1]*arrayMatriks[3][1]
        
print(hasil1,hasil3)
print(hasil2,hasil4)


