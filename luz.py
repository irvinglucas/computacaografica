from OpenGL.GL import *
from OpenGL.GLU import *

def iluminacao_da_cena(estadoluz0,estadoluz1,estadoluz2):
    
    luzAmbiente0=[0.2,0.2,0.2,1.0]
    luzDifusa0=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular0 = [0.01, 0.01, 0.01, 0.01]  #;// "brilho"
    posicaoLuz0=[0.0, 50.0, 50.0, 1.0]

    luzAmbiente1=[0.0,0.0,0.0,1.0]
    luzDifusa1=[0.0,0.0,1.0,1.0]  # ; // "cor"
    luzEspecular1 = [0.0, 0.0, 0.01, 0.01]  #;// "brilho"
    posicaoLuz1=[0.0, 50.0, -50.0, 1.0]

    luzAmbiente2=[0.0,0.0,0.0,1.0]
    luzDifusa2=[1.0,0.0,0.0,1.0]  # ; // "cor"
    luzEspecular2 = [0.01, 0.0, 0.0, 0.01]  #;// "brilho"
    posicaoLuz2=[0.0, 5.0, 0.0, 0.0]  # última coord como 0 pra funcionar como vetor da luz direcional
    direcao2 = [0.0, -1,0, 0,0]  # direção do vetor do spot

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 20

    # Especifica que a cor de fundo da janela será branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita o modelo de colorização
    glShadeModel(GL_SMOOTH)   # GL_SMOOTH ou GL_FLAT

    #  Define a refletância do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    #  Define a concentração do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente0)

    # Define os parametros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa0 )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular0 )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz0 )

    # Define os parametros da luz de número 1
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa1 )
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular1 )
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1 )
    
    # Define os parametros da luz de número 2
    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente2)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa2 )
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular2 )
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2 )
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, direcao2); #direcao da luz
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 5); # angulo do cone, de 0 a 180. 
    

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    
    # Habilita a luz de número 0
    if estadoluz0 == 1:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)
        
    # Habilita a luz de número 1
    if estadoluz1 == 1:
        glEnable(GL_LIGHT1)
    else:
        glDisable(GL_LIGHT1)

    # Habilita a luz de número 2
    if estadoluz2 == 1:
        glEnable(GL_LIGHT2)
        #print('Luz Spot ligada.')
    else:
        glDisable(GL_LIGHT2)
    
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)