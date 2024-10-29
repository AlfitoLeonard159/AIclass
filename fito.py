#Nama: Alfito Leonard_F55123060
#Kelas: TI C
a = [2, 4, 5, 21, 7, 5, 2, 2, 5]

x = 2

jumlah_kemunculan = 0
indeks = []

for i in range(len(a)):
    if a[i] == x:
        jumlah_kemunculan += 1
        indeks.append(i)

# Menampilkan hasi
print(f"Variabel x = {jumlah_kemunculan} indeks {', '.join(map(str, indeks))}")
