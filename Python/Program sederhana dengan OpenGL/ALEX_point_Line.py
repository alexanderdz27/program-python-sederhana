from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-10.0,10.0,-10.0,10.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1)

    glBegin(GL_LINES)
    glVertex2f(-5.0,0.0) 
    glVertex2f(-3.47,3.95) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-2.0,0.0) 
    glVertex2f(-3.47,3.95) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.2535,1.99535) 
    glVertex2f(-2.7624,1.99535) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-1.5,4.0) 
    glVertex2f(-1.5,0.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.6,0.0) 
    glVertex2f(-1.5,0.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(1.0,4.0) 
    glVertex2f(1.0,0.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.0,4.0) 
    glVertex2f(1.0,4.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(1.0,2.0) 
    glVertex2f(3.0,2.0)
    glEnd()    

    glBegin(GL_LINES)
    glVertex2f(3.0,0.0) 
    glVertex2f(1.0,0.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.5,4.0) 
    glVertex2f(7.0,0.0)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.5,0.0) 
    glVertex2f(7.0,4.0)
    glEnd()

    glFlush()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(1000,1000)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Plot Origin  | Naseem's OpenGLlabs")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()

main()
