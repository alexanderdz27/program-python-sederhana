import re

angka = []
for i in range(1,1001):
    angka.append(i)

String = ""
for j in angka:
    String = String + str(j) + " "

gabungan_angka = re.sub(r'\s+', '', String.rstrip())

print(gabungan_angka[1110:1111])