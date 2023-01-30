from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-20.0,20.0,-30.0,20.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(1)

    glBegin(GL_LINES)
    glVertex2f(-5.5,5.0) 
    glVertex2f(-4.8,-0.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(5.5,5.0) 
    glVertex2f(4.8,-0.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-5.5,5.0) 
    glVertex2f(-3.25,5.0) 
    glEnd()    

    glBegin(GL_LINES)
    glVertex2f(5.5,5.0) 
    glVertex2f(3.25,5.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.25,5.0) 
    glVertex2f(-3.25,4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.25,5.0) 
    glVertex2f(3.25,4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.25,4.0) 
    glVertex2f(0.0,0.35) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.25,4.0) 
    glVertex2f(0.0,0.35) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.0,4.0) 
    glVertex2f(0.0,0.7) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.0,4.0) 
    glVertex2f(0.0,0.7) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.0,4.0)
    glVertex2f(-3.25,4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.0,4.0)
    glVertex2f(3.25,4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.0,0.0) 
    glVertex2f(-4.8,-0.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(4.0,0.0) 
    glVertex2f(4.8,-0.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.0,0.0) 
    glVertex2f(-4.25,4.45) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(4.0,0.0) 
    glVertex2f(4.25,4.45) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-5.25,5.0) 
    glVertex2f(-4.25,4.45) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(5.25,5.0) 
    glVertex2f(4.25,4.45) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-2.55,5.15) 
    glVertex2f(-3.0,4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(2.55,5.15) 
    glVertex2f(3.0,4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-2.55,5.15) 
    glVertex2f(-1.73,5.28) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(2.55,5.15) 
    glVertex2f(1.73,5.28) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.72,5.44) 
    glVertex2f(-1.73,5.28) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.72,5.44) 
    glVertex2f(1.73,5.28) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-0.72,5.44) 
    glVertex2f(0.0,5.6) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.72,5.44) 
    glVertex2f(0.0,5.6) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.0,4.0) 
    glVertex2f(-2.2,4.45) 
    glEnd()


    glBegin(GL_LINES)
    glVertex2f(3.0,4.0) 
    glVertex2f(2.2,4.45) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-1.0,4.68) 
    glVertex2f(-2.2,4.45) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(1.0,4.68) 
    glVertex2f(2.2,4.45) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-1.0,4.68) 
    glVertex2f(0.0,4.85) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(1.0,4.68) 
    glVertex2f(0.0,4.85) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.0,4.0) 
    glVertex2f(0.0,1.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.0,4.0) 
    glVertex2f(0.0,1.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-1.5,3.6) 
    glVertex2f(-0.9,3.75) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(1.5,3.6) 
    glVertex2f(0.9,3.75) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-1.5,3.6) 
    glVertex2f(0.0,2.43) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(1.5,3.6) 
    glVertex2f(0.0,2.43) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-1.5,3.6) 
    glVertex2f(0.0,2.6) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(1.5,3.6) 
    glVertex2f(0.0,2.6) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.0,3.8) 
    glVertex2f(-0.9,3.75) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(0.0,3.8) 
    glVertex2f(0.9,3.75) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.0,0.0) 
    glVertex2f(-2.55,-0.99) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(4.0,0.0) 
    glVertex2f(2.55,-0.99) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.15,-1.2) 
    glVertex2f(-4.8,-0.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(4.15,-1.2) 
    glVertex2f(4.8,-0.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-1.0,-0.99) 
    glVertex2f(-2.55,-0.99) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(1.0,-0.99) 
    glVertex2f(2.55,-0.99) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.0,-1.6) 
    glVertex2f(-2.55,-0.99) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.0,-1.6) 
    glVertex2f(2.55,-0.99) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.0,-1.6) 
    glVertex2f(-3.0,-1.2) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.0,-1.6) 
    glVertex2f(3.0,-1.2) 
    glEnd()



    glBegin(GL_LINES)
    glVertex2f(-1.0,-0.99) 
    glVertex2f(-1.4,-1.6) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(1.0,-0.99) 
    glVertex2f(1.4,-1.6) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.0,-1.6) 
    glVertex2f(-1.4,-1.6) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.0,-1.6) 
    glVertex2f(1.4,-1.6) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.7,-1.0) 
    glVertex2f(-3.0,-1.2) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.7,-1.0) 
    glVertex2f(3.0,-1.2) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.7,-1.0) 
    glVertex2f(-4.7,-1.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.7,-1.0) 
    glVertex2f(4.7,-1.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.5,-4.4) 
    glVertex2f(-4.7,-1.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(4.5,-4.4) 
    glVertex2f(4.7,-1.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.5,-4.4) 
    glVertex2f(-4.0,-4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(4.5,-4.4) 
    glVertex2f(4.0,-4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.15,-1.2)
    glVertex2f(-4.0,-4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(4.15,-1.2)
    glVertex2f(4.0,-4.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.5,-4.5) 
    glVertex2f(-3.5,-5.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(4.5,-4.5) 
    glVertex2f(3.5,-5.5) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-4.0,-4.0) 
    glVertex2f(-3.0,-5.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(4.0,-4.0) 
    glVertex2f(3.0,-5.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.5,-5.5)  
    glVertex2f(-3.0,-5.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.5,-5.5)  
    glVertex2f(3.0,-5.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.0,-1.6) 
    glVertex2f(-2.4,-2.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.0,-1.6) 
    glVertex2f(2.4,-2.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-3.0,-1.6) 
    glVertex2f(-3.0,-6.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(3.0,-1.6) 
    glVertex2f(3.0,-6.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-2.2,-7.2) 
    glVertex2f(-3.0,-6.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(2.2,-7.2) 
    glVertex2f(3.0,-6.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-2.5,-5.4) 
    glVertex2f(-3.0,-6.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(2.5,-5.4) 
    glVertex2f(3.0,-6.0) 
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-2.5,-5.4) 
    glVertex2f(-3.0,-6.0) 
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
