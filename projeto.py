# Aula sobre composicao de objetos e uso do teclado.


from math import cos
from math import pi
from math import sin
from PIL import Image as Image
import timeit
import numpy
import ctypes
import random
import sys
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global esqdir
global cimabaixo
global aux1
global aux2
global angulo
global distanciamax
global estadoluz0
global estadoluz1
global estadoluz2

esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 45
distanciamax = 500    #distancia max para renderizar objs na proj. testar com 10.
estadoluz0 = 1
estadoluz1 = 0
estadoluz2 = 0

def eixos():      #desenha os eixos x e y do plano cartesiano.
    glColor3f(.9, .1, .1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotacao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtacao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .1, .9) # cor RGB  eixo Y
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotacao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtacao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .9, .1) # cor RGB  eixo z
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    #glRotatef(90, 1.0, 0.0, 0.0)     #Rotacao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtacao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix() 

def pisocomum():
    glColor3f(0.7, 0.7, 0.7) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformacoes no objeto
    glTranslate( 0.0, -1.0, 0.0)  #Transtacao do objeto
    #glRotatef(-90, 1.0, 0.0, 0.0)     #Rotacao do objeto
    glBegin(GL_POLYGON)
    glVertex3f( 4.0, -0.0, -4.0)       # P1
    glVertex3f( 4.0, -0.0, 4.0)       # P2
    glVertex3f( -4.0, -0.0, 4.0)       # P3
    glVertex3f( -4.0, -0.0, -4.0)       # P4
    glEnd()
    glPopMatrix()

def pisotextura():
    #glColor3f(0.7, 0.7, 0.7) # cor RGB
    glPushMatrix()
    glTranslate( 0.0, -1.0, 0.0)  #Transtacao do objeto
    # Textured 
    tex = read_texture('tijolo_pedra.jpg')   # testar com tijolo_pedra.jpg  e xadrez.jpg
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex)
    
    glBegin(GL_POLYGON)
    #gluCylinder(textura, largura da base, largura do topo, altura, resolucao , resolucao)
    glTexCoord2f (0.0, 0.0);
    glVertex3f(4.0, 0.0, -4.0)

    glTexCoord2f (3.0, 0.0);
    glVertex3f(4.0, 0.0, 4.0)

    glTexCoord2f (3.0, 3.0);
    glVertex3f(-4.0, 0.0, 4.0)

    glTexCoord2f (0.0, 3.0);
    glVertex3f(-4.0, 0.0, -4.0)
    glEnd()


    glDisable(GL_TEXTURE_2D)   
    glPopMatrix()


def read_texture(filename):
      img = Image.open(filename)
      img_data = numpy.array(list(img.getdata()), numpy.int8)
      textID = glGenTextures(1)
      glBindTexture(GL_TEXTURE_2D, textID)
      glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
      #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)    #  Opcao para Truncar a figura
      #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)      
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)   #  Opcao para repetir a figura
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
      glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
      glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
      #glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_REPLACE)
      #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
      #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_SPOT_DIRECTIONAL)
      glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
      return textID




def desenhotextura3():
    glPushMatrix()
    glTranslatef(1, 0, -1)
    # Textured 
    tex = read_texture('parede.jpg')
    #qobj = gluNewQuadric()
    #gluQuadricTexture(qobj, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex)
    
    glBegin(GL_POLYGON)
    #gluCylinder(textura, largura da base, largura do topo, altura, resolucao , resolucao)
    glTexCoord2f (0.0, 0.0);
    glVertex3f(0.0, 0.0, 0.0)

    glTexCoord2f (3.0, 0.0);
    glVertex3f(3.0, 0.0, 0.0)

    glTexCoord2f (3.0, 3.0);
    glVertex3f(3.0, 3.0, 0.0)

    glTexCoord2f (0.0, 3.0);
    glVertex3f(0.0, 3.0, 0.0)
    glEnd()

    #gluDeleteQuadric(qobj)

    glDisable(GL_TEXTURE_2D)   
    glPopMatrix()
    #glutSwapBuffers()


# OBJETOS GLU

# To draw a sphere :
#     glu.gluSphere(quadric, radius, slices, rings)
# To draw a cylinder (or a cone if a radius is equal to 0) :
#     glu.gluCylinder(quadric, bottomRadius, topRadius, height, slices, rings)
# To draw a CD (or a disk if internalRadius is equal to 0) :
#     glu.gluDisk(quadric, internalRadius, externalRadius, slices, rings)
# To draw a partial CD (or a piece of a disk) :
#     glu.gluPartialDisk(quadric, internalRadius, externalRadius, slices, rings, startAngle, angle)



def desenhotextura2():
    glPushMatrix()
    glTranslatef(3, 0, 1)
    # Textured 
    tex = read_texture('textura_azul.jpg')
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    #Estilo do desenho GLU_FILL (solido), GLU_LINE (wireframe), GLU_SILHOUETTE (desenha somente a silhueta) e GLU_POINT (desenha somente os vertices)
    gluQuadricDrawStyle (qobj, GLU_FILL) 
    gluQuadricNormals (qobj, GLU_SMOOTH)  # Vetores nomais.  GLU_FLAT = por face. GLU_SMOOTH = por vertice


    glEnable(GL_TEXTURE_2D)  
    glBindTexture(GL_TEXTURE_2D, tex)
    
    #gluCylinder(textura, largura da base, largura do topo, altura, resolucao , resolucao)
    
    gluCylinder(qobj, 1 , 1, 1, 20, 20)
    
    gluDeleteQuadric(qobj)
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    #glutSwapBuffers()

def desenhotextura():
    glPushMatrix()
    glTranslatef(1, 0, 0)
    glRotatef(90, 1, 0, 0)
    # Textured 
    tex = read_texture('mundo.jpg')
    qobj = gluNewQuadric()
    gluQuadricTexture(qobj, GL_TRUE)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, tex)

    gluSphere(qobj, 1, 20, 20)
    
    gluDeleteQuadric(qobj)
    glDisable(GL_TEXTURE_2D)    
    glPopMatrix()
    #glutSwapBuffers()


#def esferacomum():
    # Esfera comum
#    glPushMatrix()
#    color = [0.4, 0.4, 0.2, 1.0]
#    glMaterialfv(GL_FRONT, GL_DIFFUSE, color)
#    glTranslatef(-2, 0, 0)
#    glutSolidSphere(1, 100, 20)
#    glPopMatrix()

def paredeFundo():
    
    glColor3f(1, 1, 1)  
    glPushMatrix()              
    glTranslate( 0,2.2,-4)  
    glRotatef(0, 0, 1, 0.0)  
    glScalef(80,65.5,1)
    glutSolidCube(0.1)
    
    glPopMatrix()

def paredeLateralDireita():
    
    glColor3f(1, 1, 1)  
    glPushMatrix()              
    glTranslate( 3.95,2.2,0)  
    glRotatef(90, 0, 1, 0)  
    glScalef(79.5,64.5,1)
    glutSolidCube(0.1)
    
    glPopMatrix()

def paredeLateralEsquerda():
    
    glColor3f(1, 1, 1)  
    glPushMatrix()              
    glTranslate( -3.95, 2.2,0)  
    glRotatef(90, 0, 1, 0)  
    glScalef(79.5,64.5,1)
    glutSolidCube(0.1)
    
    glPopMatrix()


def desenho():
    global aux1
    global aux2
    
    # Objetos desenhados
    eixos()
    #esferacomum()
    paredeFundo()
    paredeLateralDireita()
    paredeLateralEsquerda()
    #desenhotextura()   # esferas
    #desenhotextura2()   # cilindro
    #desenhotextura3()   # parede
    #pisocomum()
    pisotextura()

    # Opcoes de objetos (Exemplos):
    
    #glutSolidSphere( 0.5,50,50)
    #glutSolidSphere(0.5,100,100)
    #glutWireTorus(0.3,0.9,100,10)   # rosquinha   
    # glutSolidTorus(0.5,0.5,100,100)
    # glutWireIcosahedron(1)
    #glutSolidIcosahedron(1)  
    #glutWireDodecahedron(1)
    # glutSolidDodecahedron(0.5)
    #glutWireCone(0.5, 1.0, 40, 20)   # piramides e cones  (tamanho da base, altura, lados , camadas )
    #glutSolidCone(0.5, 1.0, 40, 40)
    # glutWireCube(0.3,0.5)
    #glutSolidCube(0.5)
    #glutSolidCylinder(0.5, 0.1, 30, 30)


# ILUMINAcaO E APAReNCIA DOS OBJETOS

def iluminacao_da_cena():
    
    luzAmbiente0=[0.2,0.2,0.2,1.0]
    luzDifusa0=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular0 = [1.0, 1.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz0=[0.0, 50.0, 50.0, 1.0]

    luzAmbiente1=[0.0,0.0,0.0,1.0]
    luzDifusa1=[0.0,0.0,1.0,1.0]  # ; // "cor"
    luzEspecular1 = [0.0, 0.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz1=[0.0, 50.0, -50.0, 1.0]

    luzAmbiente2=[0.0,0.0,0.0,1.0]
    luzDifusa2=[1.0,0.0,0.0,1.0]  # ; // "cor"
    luzEspecular2 = [1.0, 0.0, 0.0, 1.0]  #;// "brilho"
    posicaoLuz2=[0.0, 5.0, 0.0, 0.0]  # ultima coord como 0 pra funcionar como vetor da luz direcional
    direcao2 = [0.0, -1,0, 0,0]  # direcao do vetor do spot

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    # Especifica que a cor de fundo da janela sera branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita o modelo de colorizacao
    glShadeModel(GL_SMOOTH)   # GL_SMOOTH ou GL_FLAT

    #  Define a refletancia do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    #  Define a concentracao do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente0)

    # Define os parametros da luz de numero 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa0 )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular0 )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz0 )

    # Define os parametros da luz de numero 1
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa1 )
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular1 )
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1 )
    
    # Define os parametros da luz de numero 2
    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente2)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa2 )
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular2 )
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2 )
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, direcao2); #direcao da luz
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 5); # angulo do cone, de 0 a 180. 
    

    # Habilita a definicao da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminacao
    glEnable(GL_LIGHTING)
    
    # Habilita a luz de numero 0
    if estadoluz0 == 1:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)
        
    # Habilita a luz de numero 1
    if estadoluz1 == 1:
        glEnable(GL_LIGHT1)
    else:
        glDisable(GL_LIGHT1)

    # Habilita a luz de numero 2
    if estadoluz2 == 1:
        glEnable(GL_LIGHT2)
        print('Luz Spot ligada.')
    else:
        glDisable(GL_LIGHT2)
    
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


def tela():
    global angulo
    global distanciamax
    global aux1
    global aux2

# AJUSTE DE APAReNCIA

    # Especifica que a cor de fundo da janela sera branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projecao
    glLoadIdentity()# carrega a matriz identidade

    #gluPerspective(angulo, aspecto , near (perto), far(longe) )
    #  angulo = angulo em graus na direcao y.
    #  aspecto = deformacao da janela. normalmente e a razao entre a largura e altura
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado
    gluPerspective(angulo, 1, 0.1, distanciamax) # Especifica a projecao perspectiva

    #glOrtho(left,right,bottom, top, near, far)
    #  left,right,bottom, top = limites da projecao
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado 
    #glOrtho(-5,5,-5,5,0.1,500) # Especifica a projecao paralela ortogonal

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

#CaMERA

    #Pense na camera como um vetor que aponta para o alvo da cena. #
    #Cada ponto desse vetor e em 3D (x, y, z)
    # A ultima coordenada ajusta a posicao da camera (deitada, de pe, invertida etc)

    #gluLookAt(eyex, eyey, eyez, alvox, alvoy, alvoz, upx, upy, upz)
    #    eyex, eyey, eyez = posicao da camera
    #    alvox, alvoy, alvoz = coordenada para onde a camera olha.
    #    upx, upy, upz = indica a posicao vertical da camera.
    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posicao do observador e do alvo
    print('Camera: (' + str( sin(esqdir) * 10) + ',' + str(cimabaixo) + "," + str(cos(esqdir) * 10) + ')')
    print('Alvo: (' + str(aux1) +','+str(aux2)+',0)')

   
    
    iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho


# FUNcoES DO TECLADO E MOUSE    

# Funcao callback chamada para gerenciar eventos de teclas normais
# Obs.: maiusculo e minusculo faz diferenca.
def Teclado (tecla, x, y):
    global aux1
    global aux2
    global estadoluz0
    global estadoluz1
    global estadoluz2
    #print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ",tecla)
	
    if tecla==chr(27): # ESC ?
        sys.exit(0)
    if tecla == b'a':  # A
        aux1 = aux1 - 0.1
        print ("aux1 = ", aux1 )
    if tecla == b's': # S
        aux1 = aux1 + 0.1
        print ("aux1 = ", aux1 )
    if tecla == b'w': # W
        aux2 = aux2 + 0.1
        print ("aux2 = ", aux2 )
    if tecla == b'z': # Z
        aux2 = aux2 - 0.1
        print ("aux2 = ", aux2 )
    if tecla == b'0': # 0
        if estadoluz0 == 0:
            estadoluz0 = 1
            glEnable(GL_LIGHT0)
        else:
            estadoluz0 = 0
            glDisable(GL_LIGHT0)
    if tecla == b'1': # 1
        if estadoluz1 == 0:
            estadoluz1 = 1
            glEnable(GL_LIGHT1)
        else:
            estadoluz1 = 0
            glDisable(GL_LIGHT1)
    if tecla == b'2': # 2
        if estadoluz2 == 0:
            estadoluz2 = 1
            glEnable(GL_LIGHT2)
        else:
            estadoluz2 = 0
            glDisable(GL_LIGHT2)
        
    tela()
    glutPostRedisplay()

# Funcao callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    print("*** Tratamento de teclas especiais")
    print ("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.05
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.05
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()   

# Funcao callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN): 
            if (angulo >= 10):
                angulo -= 2
		
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):   # Zoom-out
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()


# PROGRAMA PRINCIPAL

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow(b"Aula 11 - Textura")
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laco de eventos da GLUT




