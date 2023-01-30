#                   ----- Print, Tipe Data , Input -----

# print("Hello World")
# a = 12
# b = 6
# c = a/b
# print(type(c)) 

#input
# a = int(input('a ='))
# b = int(input('b ='))
# c = a*b
# print(c)


#                   ----- percabangan(if,elif,else) -----
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))

# if a > b :
#     print('halo') 
# elif a > c :
#     print('hello')
# elif b == c :
#     print('hello world')
# else :
#     print('123')


# buatlah program untuk menghitung nilai akhir seorang siswa 
# jika rata rata siswa tersebut sama dengan 100 maka siswa tersebut mendapatkan predikat A
# jika rata rata siswa tersebut kurang dari 100 atau lebih besar dari 89 maka siswa tersebut mendapatkan predikat AB
# jika rata rata siswa tersebut kurang dari 90 dan lebih besar dari 79 maka siswa tersebut mendapatkan predikat B
# jika rata rata siswa tersebut kurang dari 80 dan lebih besar dari 69 maka siswa tersebut mendapatkan predikat BC
# jika rata rata siswa tersebut kurang dari 70 maka siswa tersebut mendapatkan predikat C

#program nilai akhir siswa
# a=str(input('Masukkan nama siswa    :'))
# b=int(input('Nilai UAS Siswa        :'))
# c=int(input('Nilai UTS Siswa        :'))
# d=(b+c)/2

# if (d==100):
#     print(a,' Mendapat Predikat A')
# elif (100>d>89):
#     print(a,'Anda Mendapat Predikat AB')
# elif (90>d>79):
#     print(a,'Anda Mendapat Predikat B')
# elif (80>d>69):
#     print(a,'Anda Mendapat Predikat BC')
# elif (70>d):
#     print(a,'Anda Mendapat Predikat C')


#                   ----- Perulangan -----

# Perulangan for disebut counted loop (perulangan yang terhitung), 
# sementara perulangan while disebut uncounted loop (perulangan yang tak terhitung). 
# Perbedaannya adalah 
# perulangan for biasanya digunakan untuk mengulangi kode yang sudah diketahui banyak perulangannya. 
# Sementara while untuk perulangan yang memiliki syarat dan tidak tentu berapa banyak perulangannya.


# for
# ulang = 10
# for i in range(10):
#     print('perulangan ke-'+ str(i))

# while
# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     print("Total perulagan: "+ str(hitung))
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")

#while True
# while(True):
#     print('a')

jawab = 'tidak'
hitung = 0
while(True):
    print("Total perulagan: "+ str(hitung))
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    if jawab == 'tidak':
        break