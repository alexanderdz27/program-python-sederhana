from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

def init(): 
    glClearColor(0,0,0,0)
    gluOrtho2D(-20,20,-30,20)

def berlian1():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POLYGON)
    glColor3ub(255, 0, 0)
    glVertex2f(0.0, 1.0)
    glVertex2f(-3.0, 4.0)
    glVertex2f(-2.02532, 4.42704)
    glVertex2f(-0.99361, 4.66382)
    glVertex2f(0.0, 4.9)
    glVertex2f(1.00216, 4.64691)
    glVertex2f(2.01696, 4.44395)
    glVertex2f(3, 4)
    glEnd()

    glBegin(GL_LINES)
    glColor3ub(0, 255, 0)

    glVertex2f(0.0, 1.0)
    glVertex2f(-3.0, 4.0)

    glVertex2f(-3.0, 4.0)
    glVertex2f(-2.02532, 4.42704)

    glVertex2f(-2.02532, 4.42704)
    glVertex2f(-0.99361, 4.66382)

    glVertex2f(-0.99361, 4.66382)
    glVertex2f(0.0, 4.9)

    glVertex2f(0.0, 4.9)
    glVertex2f(1.00216, 4.64691)

    glVertex2f(1.00216, 4.64691)
    glVertex2f(2.01696, 4.44395)

    glVertex2f(2.01696, 4.44395)
    glVertex2f(3.0, 4.0)

    glVertex2f(3.0, 4.0)
    glVertex2f(0.0, 1.0)
    glEnd()

    glFlush()

def berlian2():
    glBegin(GL_POLYGON)
    glColor3ub(0,0,255)
    glVertex2f(-2.02532, 4.42704)
    glVertex2f(-3.0, 4.0)
    glVertex2f(-2.51581, 5.00209)
    glVertex2f(-1.70397, 5.25579)
    glVertex2f(-0.72299, 5.42492)
    glVertex2f(0.0, 5.5)
    glVertex2f(0.0, 4.9)
    glVertex2f(-0.99361, 4.66382)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3ub(100,100,0)
    glVertex2f(0.74847, 5.3911)
    glVertex2f(1.57722, 5.22196)
    glVertex2f(2.52436, 4.95135)
    glVertex2f(3.0, 4.0)
    glVertex2f(2.01696, 4.44395)
    glVertex2f(1.00216, 4.64691)
    glVertex2f(0.0, 4.9)
    glVertex2f(0.0, 5.5)
    glVertex2f(0.74847, 5.3911)
    glVertex2f(1.57722, 5.22196)
    glVertex2f(2.52436, 4.95135)
    glEnd()

    glBegin(GL_LINES)
    glColor3ub(0,255,255)

    glVertex2f(0.0, 4.9)
    glVertex2f(-0.99361, 4.66382)

    glVertex2f(-0.99361, 4.66382)
    glVertex2f(-2.02532, 4.42704)

    glVertex2f(-2.02532, 4.42704)
    glVertex2f(-3.0, 4.0)
    
    glVertex2f(-3.0, 4.0)
    glVertex2f(-2.51581, 5.00209)

    glVertex2f(-2.51581, 5.00209)
    glVertex2f(-1.70397, 5.25579)

    glVertex2f(-1.70397, 5.25579)
    glVertex2f(-0.72299, 5.42492)

    glVertex2f(-0.72299, 5.42492)
    glVertex2f(0.0, 5.5)

    glVertex2f(0.0, 5.5)
    glVertex2f(0.74847, 5.3911)

    glVertex2f(0.74847, 5.3911)
    glVertex2f(1.57722, 5.22196)

    glVertex2f(1.57722, 5.22196)
    glVertex2f(2.52436, 4.95135)

    glVertex2f(2.52436, 4.95135)
    glVertex2f(3.0, 4.0)

    glVertex2f(3.0, 4.0)
    glVertex2f(2.01696, 4.44395)

    glVertex2f(2.01696, 4.44395)
    glVertex2f(1.00216, 4.64691)

    glVertex2f(1.00216, 4.64691)
    glVertex2f(0.0, 4.9)
    glEnd()

    glFlush()


def berlian3():
    glBegin(GL_POLYGON)
    glColor3ub(100, 100, 100)
    glVertex2f(-0.00616, 2.60724)
    glVertex2f(-1.51344, 3.59687)
    glVertex2f(-0.00616, 2.60724)
    glEnd()
    glFlush()


def berlian4():
    glBegin(GL_POLYGON)
    glColor3ub(0,0,255)
    glVertex2f(-0.00616, 2.60724)
    glVertex2f(-3.0, 4.0)
    glVertex2f(0.0, 1.0)
    glVertex2f(3.0, 4.0)
    glEnd()
    glFlush()





def gabung():
    berlian1()
    berlian2()
    berlian3()
    berlian4()


def main():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(720,480)
    glutInitWindowPosition(270,120)
    glutCreateWindow("Plot Origin  | OpenGLlabs")
    glutDisplayFunc(gabung)
    init()
    glutMainLoop()
    

main()