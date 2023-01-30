x1=int(input("x1= "))
x2=int(input("x2= "))
y1=int(input("y1= "))
y2=int(input("y2= "))
def jarak_dua_titik(x1,x2,y1,y2):
    hasil = (((x2-x1)**2 / (y2-y1)**2)**1/2)
    return hasil;

print(jarak_dua_titik(x1,x2,y1,y2))