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
    glBegin(GL_POLYGON)
    glColor3ub(0, 100, 50)
    glVertex2f(3.0,4.0) 
    glVertex2f(4.0,5.0)
    glColor3ub(0,200,200) 
    glVertex2f(5.0,5.0) 
    glVertex2f(6.0,5.0) 
    glVertex2f(7.0,5.0)
    glColor3ub(0,0,150) 
    glVertex2f(8.0,4.0)
    glVertex2f(5.5,0.0)  
    glEnd()

    glBegin(GL_LINES)
    glColor3ub(255,255,255) 
    glVertex2f(3.0,4.0) 
    glVertex2f(4.0,5.0)

    glVertex2f(5.0,5.0) 
    glVertex2f(4.0,5.0)

    glVertex2f(5.0,5.0) 
    glVertex2f(6.0,5.0)

    glVertex2f(6.0,5.0) 
    glVertex2f(7.0,5.0)

    glVertex2f(7.0,5.0) 
    glVertex2f(8.0,4.0)

    glVertex2f(5.5,0.0) 
    glVertex2f(8.0,4.0)

    glVertex3f(5.5,0.0,-10.0) 
    glVertex3f(7.0,5.0,-10.0)

    glVertex3f(5.5,0.0,-10.0) 
    glVertex3f(6.0,5.0,-10.0)

    # glVertex2f(5.5,0.0) 
    # glVertex2f(5.0,5.0)

    # glVertex2f(5.5,0.0) 
    # glVertex2f(4.0,5.0)

    glVertex2f(5.5,0.0) 
    glVertex2f(3.0,4.0)

    # glVertex2f(8.0,4.0) 
    # glVertex2f(3.0,4.0)

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
