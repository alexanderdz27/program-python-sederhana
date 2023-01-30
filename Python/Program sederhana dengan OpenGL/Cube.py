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

    glBegin(GL_QUADS)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(2.0,0.0,0.0)
    glVertex3f(2.0,2.0,0.0)
    glVertex3f(0.0,2.0,0.0)
    glEnd()
    glFlush()

    glBegin(GL_IMAGE_CUBE)       
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(2.0,0.0,0.0)
    glVertex3f(0.0,0.0,2.0)
    glVertex3f(2.0,0.0,2.0)
    glEnd()
    glFlush()

    glVertex3f(0.0,0.0,0.0)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(0.0,0.0,0.0)
    glVertex3f(0.0,0.0,0.0)

    glVertex3f(0.0,0.0,0.0)
    glVertex3f(0.0,0.0,0.0)
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
