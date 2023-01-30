alas = 10
tinggi = 10

def luas_segitiga(alas,tinggi):
    luas= 0
    for i in range (tinggi):
        luas+= alas
    return luas/2



print(luas_segitiga(alas,tinggi))