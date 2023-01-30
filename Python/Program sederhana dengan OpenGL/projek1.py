from os import X_OK
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

pos_x = 0
pos_y = 0

xx = 50
yy = 50

hijau = 0
biru = 0
merah = 0

def init():
    glClearColor(1.0, 0.0, 1.0, 1.0)
    gluOrtho2D(-500.0, 500.0, -500.0, 500.0)

def kotak():
    global pos_x, pos_y
    glColor3f(hijau,biru,merah)
    glBegin(GL_POLYGON)

    #kiri bawah
    glVertex2f(-10 + pos_x,-10 + pos_y)
    glVertex2f(-22.99786 + pos_x,-9.70921 + pos_y)
    glVertex2f(-30 + pos_x,-10 + pos_y)
    glVertex2f(-29.6164 + pos_x,-4.41438 + pos_y)
    glVertex2f(-31.93289 + pos_x,-0.93965 + pos_y)
    glVertex2f(-36.73133 + pos_x,-0.77418 + pos_y)
    glVertex2f(-40.0406 + pos_x,-4.08345 + pos_y)
    glVertex2f(-40 + pos_x,-10 + pos_y)
    glVertex2f(-50 + pos_x,-10 + pos_y)

    # Kiri Atas
    glVertex2f(-50 + pos_x,-10 + pos_y)
    glVertex2f(-43.03992 + pos_x,15.04142 + pos_y)
    glVertex2f(-25.81074 + pos_x,19.24689 + pos_y)
    glVertex2f(-10 + pos_x,20 + pos_y)
    # Kanan Atas
    glVertex2f(5.95823 + pos_x,16.59948 + pos_y)
    glVertex2f(17.54067 + pos_x,9.98094 + pos_y)
    glVertex2f(30 + pos_x,10 + pos_y)
    glVertex2f(45.66946 + pos_x,5.1825 + pos_y)
    glVertex2f(50 + pos_x,0 + pos_y)
    # Kanan Bawah
    glVertex2f(50 + pos_x,-3.75253 + pos_y)
    glVertex2f(44.1961 + pos_x,-8.73521 + pos_y)
    glVertex2f(33.34493 + pos_x,-10.21461 + pos_y)
    glVertex2f(33.80301 + pos_x,-5.08142 + pos_y)
    glVertex2f(32.4868 + pos_x, -2.97549 + pos_y)
    glVertex2f(28.96206 + pos_x,-1.38162 + pos_y)
    glVertex2f(24.90084 + pos_x,-1.91135 + pos_y)
    glVertex2f(23.66481 + pos_x,-5.0897 + pos_y)
    glVertex2f(23.79985 + pos_x, -10.21461 + pos_y)
    
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(-500.0, 0.0)
    glVertex2f(500.0, 0.0)
    glVertex2f(0.0, 500.0)
    glVertex2f(0.0, -500.0)
    glEnd()
    glPushMatrix()
    kotak()
    glPopMatrix()
    glFlush()

def input_mouse(button, state, x, y):
    global hijau, biru, merah
    # Saat mengklik kanan warna kotak akan berubah menjadi warna biru dan merah
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        glScalef(2.0, 2.0, 0.0)
    # Saat mengklik kiri warna kotak akan berubah menjadi warna hijau dan hitam
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        glScalef(0.5, 0.5, 0.0)

def input_keyboard(key,x,y):
    global pos_x, pos_y
    global xx, yy
    # Untuk mengubah posisi kotak
    if key == GLUT_KEY_UP:
        pos_y += 5
        print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_DOWN:
        pos_y -= 5
        print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_RIGHT:
        pos_x += 5
        print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_LEFT:
        pos_x -= 5
        print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)

    # Untuk Mengubah Warna backgorund window

def input_keyboard(key,x,y):
    global pos_x, pos_y
    # Untuk mengubah posisi kotak
    if key == GLUT_KEY_UP:
        pos_y += 5
        print("Tombol Atas ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_DOWN:
        pos_y -= 5
        print("Tombol Bawah ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_RIGHT:
        pos_x += 5
        print("Tombol Kanan ditekan ", "x : ", pos_x, " y : ", pos_y)
    elif key == GLUT_KEY_LEFT:
        pos_x -= 5
        print("Tombol Kiri ditekan ", "x : ", pos_x, " y : ", pos_y)

    # Untuk Mengubah Warna backgorund window

    # Background Kiri Atas berubah warna menjadi Hijau
    if pos_x < 0 and pos_y > 0:
        glClearColor(0.0, 1.0, 0.0, 1.0)
    # Background Kanan Atas berubah warna menjadi Biru
    if pos_x > 0 and pos_y > 0:
        glClearColor(0.0,0.0,1.0,1.0)
    # Background Kanan Bawah berubah warna menjadi Merah
    if pos_x > 0 and pos_y < 0:
        glClearColor(1.0, 0.0, 0.0, 1.0)
    # Background Kiri Bawah berubah warna menjadi Hitam
    if pos_x < 0 and pos_y < 0:
        glClearColor(1.0,0.0,1.0,1.0)

def update(value):
    global pos_x, pos_y
    # pos_x += 5
    glutPostRedisplay()
    
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Eveng Handling Keyboard & Mouse")
    glutDisplayFunc(display)
    
    glutSpecialFunc(input_keyboard)
    glutMouseFunc(input_mouse)
    
    glutTimerFunc(50, update, 0)
    
    init()
    glutMainLoop()

main()
