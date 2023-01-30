#nim kelompok
#202410103063
#202410103078
#202410103038
#202410103077
#202410103014

#tema
#seorang pemain minecraft yang telah menemukan sebuah berkian dimalam hari

#mengimport library yang dibutuhkan
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init(): #ngatur display
    glClearColor(0,0,0,0)# warna display
    gluOrtho2D(-15,15,-8,10)# besar display

def rumput():#fungsi rumput
    glClear(GL_COLOR_BUFFER_BIT)#membersihkan halaman
    glPointSize(1)#mengatur ukuran titik

    #latar rumput
    glBegin(GL_QUADS) #mulai gambar segi empat
    glColor3ub(74,111,40) #masukin warna
    
    glVertex2f(-15.0,-2.0)#mengatur koordinat 
    glVertex2f(15.0,-2.0)
    glVertex2f(15.0, -8.0)
    glVertex2f(-15.0,-8.0)
    
    glEnd()# mengakhiri koordinat
    glFlush()#memunculkan gambar

def bulan():#fungsi bulan (penjelasan seperti di fungsi rumput)
    #latar bulan
    glBegin(GL_POLYGON)#memulai gambar poligon
    glColor3f(1,5,0)
    
    glVertex2f(-13.1985660878407, 5.9977123952405)
    glVertex2f(-13.9896223601741, 6.7887686675739)
    glVertex2f(-14, 8)
    glVertex2f(-13.2293262004532, 8.5751638830836)

    glVertex2f(-13.2481568802716, 7.7089526114336)
    glVertex2f(-13.1985660878407, 7.2163666526189)
    glVertex2f(-12.7709681027956, 6.7887686675739)
    glVertex2f(-11.95853193121, 6.8315284660784)
    glVertex2f(-11.1888555581289, 7.5798249399072)

    glVertex2f(-11.1674756588766, 6.7887686675739)
    glVertex2f(-12, 6)

    glEnd()
    glFlush()

def bintang():#fungsi bintang (penjelasan seperti di fungsi rumput)
    #latar bintang
    glPointSize(5)
    glBegin(GL_POINTS)#memulai gambar titik
    glColor3f(1,1,1)
    
    
    glVertex2f(-6.6213261477735, 5.0840038144297)
    glVertex2f(-4.3594233291413, 7.7417396263226)
    glVertex2f(-2.7195437856329, 4.122695116511)
    glVertex2f(1.2387861469735, 5.3101940962929)
    glVertex2f(5.8756869251696, 7.628644485391)
    glVertex2f(12.9441332333953, 6.3845979351433)
    glVertex2f(7.7417567505412, 5.1405513848955)
    
    glEnd()
    glFlush()


def pohon():#fungsi pohon (penjelasan seperti di fungsi rumput)
    glBegin(GL_POLYGON)
    glColor3ub(0,255,0)
    glVertex2f(10.0,0.0)
    glVertex2f(8.0,0.0)
    glVertex2f(8.0,1.0)
    glVertex2f(9.0,1.0)
    glVertex2f(9.0,2.0)
    glVertex2f(10.0,2.0)
    glVertex2f(10.0,3.0)
    glVertex2f(11.0,3.0)
    glVertex2f(11.0,2.0)
    glVertex2f(12.0,2.0)
    glVertex2f(12.0,1.0)
    glVertex2f(13.0,1.0)
    glVertex2f(13.0,0.0)
    glVertex2f(11.0,0.0)
    glEnd()

    glBegin(GL_QUADS) 
    glColor3ub(150,75,0) 
    glVertex2f(10.0,0.0)
    glVertex2f(11.0,0.0)
    glVertex2f(11.0,-2.0)
    glVertex2f(10.0,-2.0)
    glEnd()
    
    glFlush()
    
# def tangan():

def berlian():#fungsi berlian (penjelasan seperti di fungsi rumput)
    glBegin(GL_POLYGON)
    glColor3ub(0, 100, 50)
    glVertex2f(0.0, -3.0)
    glVertex2f(-4.0, 1.0)
    glColor3ub(0,200,200)
    glVertex2f(-3.0, 2.0)
    glVertex2f(-2.0, 2.0)
    glColor3ub(0, 102, 255)
    glVertex2f(-1.0, 2.0)
    glVertex2f(0.0, 2.0)
    glColor3ub(0,0,255) 
    glVertex2f(1.0, 2.0)
    glVertex2f(2.0, 2.0)
    glColor3ub(0,0,150)
    glVertex2f(3.0, 2.0)
    glVertex2f(4.0, 1.0)
    glEnd()

    glFlush()

def tangan():#fungsi tangan (penjelasan seperti di fungsi rumput)
    glBegin(GL_POLYGON)
    glColor3ub(255, 204, 153)
    glVertex2f(-1.7, -6.0)
    glVertex2f(-3.6, -6.0)
    glVertex2f(-2.6, -0.4)
    glVertex2f(-1.0, -2.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(255, 204, 153)
    glVertex2f(1.7, -6.0)
    glVertex2f(3.6, -6.0)
    glVertex2f(2.6, -0.4)
    glVertex2f(1.0, -2.0)
    glEnd()
    glFlush()

def baju():#fungsi baju (penjelasan seperti di fungsi rumput)
    glBegin(GL_QUADS)
    glColor3ub(0, 204, 255)
    
    glVertex2f(-1.7, -6.0)
    glVertex2f(-3.6, -6.0)
    glVertex2f(-4.0, -8.0)
    glVertex2f(-2.0, -8.0)
    
    glEnd()

    glBegin(GL_QUADS)
    glColor3ub(0, 204, 255)
    
    glVertex2f(1.7, -6.0)
    glVertex2f(3.6, -6.0)
    glVertex2f(4.0, -8.0)
    glVertex2f(2.0, -8.0)
    
    glEnd()

    glFlush()

def gabung(): #fungsi gabung untuk menggabungkan semua fungsi yang diperlukan menjadi satu
    rumput()
    bintang()
    bulan()
    berlian()
    pohon()
    tangan()
    baju()

def main():#fungsi main untuk mengatur kodingan utama
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(600,360)#mengatur ukuran windows yang muncul
    glutInitWindowPosition(0,0)#mengatur letak windows yang muncul
    glutCreateWindow("Plot Origin  | OpenGLlabs")#mengatur nama windows yang muncul
    glutDisplayFunc(gabung)#memanggil fungsi gabung untuk dijalankan
    init()
    glutMainLoop()#melakukan perulangan agar gambar terus muncul

main()#memanggil fungsi main untuk menjalankan program