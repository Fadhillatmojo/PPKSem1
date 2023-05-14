# quiz nomer 1
hour = int(input("Starting Time(hours): "))
mins = int(input("Starting Time(minutes): "))
dura = int(input("Event Duration(minutes): "))
count = 0
# Write your code here

if 0<=hour<=23 and 0<=mins<=59: #pengecekan inputan apakah kurang jamnya 0-23 dan menitnya 0-59
    par = dura
    x = mins+dura
    while x >= 60:
        x = x - 60
        count += 1
    mins += par
    if mins>=60:
        mins = mins%60
        
    lastHour = hour + count
    if lastHour >= 24 and mins != 0:
        print("Waktu akhir = "+str(lastHour-24)+":"+str(mins))
    else:
        print("Waktu akhir = "+str(lastHour)+":"+str(mins))
else:
    print("waktu tidak valid")
    
