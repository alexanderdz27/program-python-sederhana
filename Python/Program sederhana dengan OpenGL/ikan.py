from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

x = 0
a = 3

def rasiocanvas():
    glClearColor(0.0,0.8,0.9,1.0)
    gluOrtho2D(-10.0,10,-10.0,10.0)

def gerak():
    global x, a
    x += a
    if x > 10:
        glRotate(180, 1, 0)
        a *= -1.2
    if x < -10:
        glRotate(180, 1, 0)
        a *= -1.2


def badan():
    
    global x
    glColor3ub(255, 153, 51)
    glPointSize(20.0)
    glLineWidth(2)

    glBegin(GL_LINE_STRIP)
    glVertex2f(6.0 + x, 0.4)
    glVertex2f(4.8 + x, 1.2)
    glVertex2f(3.8 + x, 1.6)
    glVertex2f(2.8 + x, 1.9)
    glVertex2f(1.8 + x, 2.2)
    glVertex2f(1.0 + x, 2.3)
    glVertex2f(-0.2 + x, 2.2)
    glVertex2f(-1.0 + x,2.0)
    glVertex2f(-1.6 + x, 1.8)
    glVertex2f(-2 + x, 1.6)
    glVertex2f(-2.4 + x, 1.4)
    glVertex2f(-2.8 + x, 1.0)
    glVertex2f(-3.0 + x, 0.6)
    glVertex2f(-3.0 + x, 0.4)
    glVertex2f(-3.0 + x, 0.2)
    glVertex2f(-2.8 + x, -0.2)
    glVertex2f(-2.4 + x, -0.6)
    glVertex2f(-2.0 + x, -0.8)
    glVertex2f(-1.6 + x, -1.0)
    glVertex2f(-1.0 + x, -1.2)
    glVertex2f(-0.2 + x, -1.4)
    glVertex2f(1.0 + x, -1.6)
    glVertex2f(1.8 + x, -1.5)
    glVertex2f(2.8 + x, -1.2)
    glVertex2f(3.8 + x, -0.8)
    glVertex2f(4.8 + x, -0.4)
    glVertex2f(6.0 + x, 0.4)
    glEnd()

def sirip_1():
    global x
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.8 + x, 2.3)
    glVertex2f(2.6 + x, 3.0)
    glVertex2f(3.4 + x, 3.2)
    glVertex2f(2.6 + x, 2.4)
    glVertex2f(4.2 + x, 2.1)
    glVertex2f(3.1 + x, 1.8)
    glEnd()

def sirip_2():
    global x
    glBegin(GL_LINE_STRIP)
    glVertex2f(1.0 + x, -1.6)
    glVertex2f(3.0 + x, -2.0)
    glVertex2f(2.0 + x, -1.4)
    glEnd()

def buntut():
    global x
    glBegin(GL_LINE_STRIP)
    glVertex2f(6.0 + x, 0.4)
    glVertex2f(7.5 + x, 2.0)
    glVertex2f(7.5 + x, -1.2)
    glVertex2f(6.0 + x, 0.4)
    glEnd()

def PartOfBody():
    global x
    glBegin(GL_POINTS)
    glVertex2f(-1.4 + x, 1.0)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glVertex2f(-0.2 + x, 2.2)
    glVertex2f(0.0 + x, 1.7)
    glVertex2f(0.2 + x, 1.2)
    glVertex2f(0.3 + x, 0.6)
    glVertex2f(0.3 + x, 0.0)
    glVertex2f(0.2 + x, -0.6)
    glVertex2f(0.0 + x, -1.1)
    glVertex2f(-0.2 + x, -1.4)
    glEnd()

def all():
    glClear(GL_COLOR_BUFFER_BIT)
    global x, a
    x += a
    if x > 9:
        
        glRotate(180,0, 1, 0)
        a *= -1
    if x < 0:
        
        glRotate(180,0, 1, 0)
        a *= -1
    
    
    badan()
    PartOfBody()
    sirip_1()
    sirip_2()
    buntut()
    
    glFlush()   
    
def update(value):

    glutPostRedisplay()
    glutTimerFunc(100,update,0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Plot Origin  | Naseem's OpenGLlabs")
    glutDisplayFunc(all)
    glutTimerFunc(50, update, 0)
    rasiocanvas()
    glutMainLoop()

main()