'''
-- Projeto Casa - Computação gráfica --

Alunos:
- Irving Lucas da Silva Melo
- Antônio Andrade
- Jonathas Augusto

- Este projeto consiste na modelagem de uma casa simples:
    - Sala de estar
    - Dois quartos
    - Banheiro
    - Cozinha


- Comandos de interação do mouse:
    - Apertar e segurar botão esquerdo: rotação da casa na cena
    - Apertar e segurar botão direito: translação da casa pela

- Comandos de interação do cubo no teclado:
    - W: para frente
    - A: para esquerda
    - D: para direita
    - S: para trás

- Comandos de iluminação

    - Ligar luz ambiente: Número 1
    - Ligar luz azul: Número 2
    - Ligar luz vermelha: Número 3
'''
from sys import argv
import sys
import pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from objloader import *
from util import *
from luz import *


glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(50, 50)
glutCreateWindow(b"Casa")

pygame.init()
pygame.mixer.init()

def som_abrir():
    pygame.mixer.music.load("abrir_porta.mp3")
    pygame.mixer.music.play(loops=0)
def som_fechar():
    pygame.mixer.music.load("fechar_porta.mp3")
    pygame.mixer.music.play(loops=0)
def som_ligar():
    pygame.mixer.music.load("acender_luz.mp3")
    pygame.mixer.music.play(loops=0)
def som_desligar():
    pygame.mixer.music.load("apagar_luz.mp3")
    pygame.mixer.music.play(loops=0)

viewport = (800, 600)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)

# Parâmetros de movimentação do cubo de interação
move_forward = False
move_back = False
move_left = False
move_right = False
move_speed = 0.1
cam_move_speed = 2.5

# Parâmetros da animação das portas
open_speed = 2
abrir_banheiro = False
abrir_quarto = False
abrir_quarto2 = False

som_porta_abrir1 = False
som_porta_abrir2 = False
som_porta_abrir3 = False
som_porta_fechar1 = False
som_porta_fechar2 = False
som_porta_fechar3 = False


contador_easteregg = 0

# Estado da iluminação
estadoluz0 = 1
estadoluz1 = 0
estadoluz2 = 0
som_ligar_luz0 = False
som_ligar_luz1 = False
som_ligar_luz2 = False


#rx, ry = (0,0)
#tx, ty = (0,0)
#zpos = 5
rx, ry = (-90, 88)
tx, ty = (4, -1)
zpos = 9

rotate = move = False

# Carregamento dos objetos
walls = [
    OBJ("wall_01.obj"),
    OBJ("wall_02.obj"),
    OBJ("wall_03.obj"),
    OBJ("wall_04.obj"),
    OBJ("wall_05.obj"),
    OBJ("wall_06.obj"),
    OBJ("wall_07.obj"),
    OBJ("wall_08.obj"),
    OBJ("wall_09.obj"),
    OBJ("wall_10.obj"),
    OBJ("wall_11.obj"),
    OBJ("wall_12.obj"),
    OBJ("wall_13.obj"),
    OBJ("wall_14.obj"),
    OBJ("wall_15.obj"),
    OBJ("wall_16.obj"),
    OBJ("wall_17.obj"),
    OBJ("wall_18.obj"),
    OBJ("wall_19.obj"),
    OBJ("wall_20.obj"),
    OBJ("wall_21.obj"),
    OBJ("wall_22.obj"),
    OBJ("wall_23.obj"),
    OBJ("wall_24.obj"),
]

door = OBJ("door.obj", scale=[.8, .8, .9], pos=[7, 0, -3.35], rot=[0, 90, 0])
door2 = OBJ("door.obj", scale=[.8, .8, .9], pos=[6.84, 0, 6.9], rot=[0, 0, 0])
door3 = OBJ("door.obj", scale=[.8, .8, .9], pos=[0, 0, -6.8], rot=[0, 0, 0])

porta_banheiro = OBJ("door.obj", scale=[.8, .8, .9], pos=[
                     0, 0, 1.2], rot=[0, 0, 0])
porta_quarto = OBJ(
    "door.obj", scale=[.8, .8, .9], pos=[-5, 0, -.9], rot=[0, 90, 0])
porta_quarto2 = OBJ(
    "door.obj", scale=[.8, .8, .9], pos=[-2.7, 0, -1.2], rot=[0, 0, 0])

clock_ = OBJ("clock.obj", pos=[-2, 3, -4])
clock_p1 = OBJ("clock_p1.obj", pos=[-2, 3, -4], rot=[0, 0, 0])
clock_p2 = OBJ("clock_p2.obj", pos=[-2, 3, -4], rot=[0, 0, 0])

window = OBJ("window.obj")
floor = OBJ("floor.obj")
couch = OBJ("couch.obj", pos=[0, 0, 0])
table = OBJ("table.obj")
scream = OBJ("ogrito.obj")
carpet = OBJ("carpet.obj")

pia = OBJ("pia.obj")
fogao = OBJ("fogao.obj",   pos=[3.20, 0.90, 1.30])
estante = OBJ("estante.obj", pos=[3.85, -0.39, 5.6])
tapete = OBJ("tapete.obj")

cama1 = OBJ("bed.obj")
wardrobe1 = OBJ("wardrobe.obj")
#dog = OBJ("13463_Australian_Cattle_Dog_v3.obj", scale=[.06, .06, .06], pos=[5, 0, 9], rot=[-90, 0, 0])
#tapetedog = OBJ("tapete.obj", pos=[-4, 0, -3], scale=[1.5, 1.5, 2])
cama2 = OBJ("bed.obj", pos=[0, 0, -10])
wardrobe2 = OBJ("wardrobe.obj", pos=[0, 0, -10])

bathtub = OBJ("bathtub.obj")
sink = OBJ("sink.obj")
toilet = OBJ("toilet.obj")

trigger_banheiro = OBJ("trigger_banheiro.obj", isTrigger=True)
trigger_quarto = OBJ("trigger_quarto.obj", isTrigger=True)
trigger_quarto2 = OBJ("trigger_quarto2.obj", isTrigger=True)
trigger_quarto3 = OBJ("trigger_quarto3.obj", isTrigger=True)

collision_mask = [couch, table, pia, fogao, estante, cama1,
                  cama2, wardrobe1, wardrobe2, bathtub, sink, toilet]
for x in range(len(walls)):
    if x not in [15, 18, 21]:
        collision_mask.append(walls[x])

personagem = OBJ("cubo.obj", pos=[0, 0, 0])

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(70.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

# Loop de verificação das interações do usuário
while True:
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN:  # Evento de pressionar as teclas
            if e.key == K_w:  # Tecla W
                move_forward = True
            elif e.key == K_s:  # Tecla S
                move_back = True
            elif e.key == K_a:  # Tecla A
                move_left = True
            elif e.key == K_d:  # Tecla D
                move_right = True
            elif e.key == K_BACKSPACE:
                sys.exit()

            if e.key == K_1:  # Tecla 1
                if estadoluz0 == 0:
                    estadoluz0 = 1
                    if som_ligar_luz0==False:
                        som_ligar()
                        som_ligar_luz0=True
                else:
                    estadoluz0 = 0
                    som_desligar()
                    som_ligar_luz0 = False

            if e.key == K_2:  # Tecla 2
                if estadoluz1 == 0:
                    estadoluz1 = 1
                    if som_ligar_luz1 == False:
                        som_ligar()
                        som_ligar_luz1 = True
                else:
                    estadoluz1 = 0
                    som_desligar()
                    som_ligar_luz1 = False
            if e.key == K_3:  # Tecla 3
                if estadoluz2 == 0:
                    estadoluz2 = 1
                    if som_ligar_luz2 == False:
                        som_ligar()
                        som_ligar_luz2 = True
                else:
                    estadoluz2 = 0
                    som_desligar()
                    som_ligar_luz2 = False

        elif e.type == KEYUP:  # Evento de soltar as teclas
            if e.key == K_w:  # Tecla W
                move_forward = False
            elif e.key == K_s:  # Tecla S
                move_back = False
            elif e.key == K_a:  # Tecla A
                move_left = False
            elif e.key == K_d:  # Tecla D
                move_right = False

        # Captação de comandos do mouse
        elif e.type == MOUSEBUTTONDOWN:  # Evento de pressionar botão do mouse
            if e.button == 4:
                zpos = max(1, zpos-1)
            elif e.button == 5:
                zpos += 1
            elif e.button == 1:
                rotate = True
            elif e.button == 3:
                move = True
        elif e.type == MOUSEBUTTONUP:  # Evento de soltar botão do mouse
            if e.button == 1:
                rotate = False
            elif e.button == 3:
                move = False
        elif e.type == MOUSEMOTION:  # Evento de captação da quantidade do movimento do mouse
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j

    # Colisão do cubo com os objetos da cena sem triggers
    a = chek_collisions(personagem, collision_mask)

    # Colisão  do cubo nas portas que abrem (triggers)
    # São dicionários que contém a colisão do cubo com as respectivas portas
    t_banheiro = chek_collisions(personagem, [trigger_banheiro])
    t_quarto = chek_collisions(personagem, [trigger_quarto2])
    t_quarto_2 = chek_collisions(personagem, [trigger_quarto3])
    t_quarto2 = chek_collisions(personagem, [trigger_quarto])

    # Verificação para animar as portas

    # banheiro
    if (t_banheiro['left'] != 0):
        abrir_banheiro = True
    else:
        abrir_banheiro = False

    # quartos
    if (t_quarto['right'] != 0 or t_quarto_2['up'] != 0):
        abrir_quarto = True
    else:
        abrir_quarto = False

    if t_quarto2['right'] != 0:
        abrir_quarto2 = True
    else:
        abrir_quarto2 = False

    # Movimentação do cubo de interação
    if move_forward and a['up'] == 0:
        personagem.pos[0] -= move_speed
        ty -= cam_move_speed

    elif move_back and a['down'] == 0:
        personagem.pos[0] += move_speed
        ty += cam_move_speed

    elif move_left and a['left'] == 0:
        personagem.pos[2] += move_speed
        tx += cam_move_speed

    elif move_right and a['right'] == 0:
        personagem.pos[2] -= move_speed
        tx -= cam_move_speed

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glPushMatrix()
    glTranslate(tx/20., ty/20., - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 1, 0)

    # Iluminação
    iluminacao_da_cena(estadoluz0, estadoluz1, estadoluz2)

    # ------------Estrutura da casa------------

    # Renderização da lista de paredes
    for wall in walls:
        wall.render()

    door.render()
    door2.render()
    door3.render()


    # Animação das portas
    # banheiro
    porta_banheiro.render()
    if(abrir_banheiro):
        if (porta_banheiro.rot[1] < 150):
            porta_banheiro.rot[1] += 1 * open_speed
        if (som_porta_abrir1 == 0 and porta_banheiro.rot[1]==2):
            som_abrir()
            som_porta_abrir1 = 1

        else:
            abrir_banheiro = False
            som_porta_abrir1 = 0
    else:
        if (porta_banheiro.rot[1] > 0):
            porta_banheiro.rot[1] -= 1 * open_speed
            if (som_porta_fechar1 == 0 and porta_banheiro.rot[1]<30):
                som_fechar()
                som_porta_fechar1 = 1
        else:
            som_porta_abrir1 = 0 
            som_porta_fechar1 = 0

    # Quarto
    porta_quarto.render()
    if(abrir_quarto):
        if (porta_quarto.rot[1] > 0):
            porta_quarto.rot[1] -= 1 * open_speed
        if (som_porta_abrir2 == 0 and porta_quarto.rot[1] == 88):
            som_abrir()
            som_porta_abrir2 = 1
        else:
            abrir_quarto = False
            som_porta_abrir2 = 0
    else:
        if (porta_quarto.rot[1] < 90):
            porta_quarto.rot[1] += 1 * open_speed
            if (som_porta_fechar2 == 0 and porta_quarto.rot[1] == 80):
                som_fechar()
                som_porta_fechar2 = 1
                
        else:
            som_porta_abrir2 = 0
            som_porta_fechar2 = 0
    # quarto 2
    porta_quarto2.render()
    if(abrir_quarto2):
        if (porta_quarto2.rot[1] > -100):
            porta_quarto2.rot[1] -= 1 * open_speed
        if (som_porta_abrir3 == 0 and porta_quarto2.rot[1] == -2):
            som_abrir()
            som_porta_abrir3 = 1
        
        else:
            abrir_quarto2 = False
            som_porta_abrir3 = 0
    else:
        if (porta_quarto2.rot[1] < 0):
            porta_quarto2.rot[1] += 1 * open_speed
            if (som_porta_fechar3 == 0 and porta_quarto2.rot[1] > -30):
                som_fechar()
                som_porta_fechar3 = 1

        else:
            som_porta_abrir3 = 0
            som_porta_fechar3 = 0
    render(floor)
    render(window)
    render(window, pos=[2.8, 0, 8])
    render(window, pos=[-1.3, 0, 0], rot=[0, 90, 0])
    render(window, pos=[-1.3, 0, 13.9], rot=[0, 90, 0])

    # Sala
    couch.render()
    table.render()
    scream.render()
    carpet.render()
    clock_.render()
    clock_p1.render()
    clock_p2.render()
    clock_p1.rot[0] -= 1
    clock_p2.rot[0] -= 2
    #dog.render()
    #tapetedog.render()

    # Cozinha
    pia.render()
    fogao.render()
    estante.render()
    tapete.render()

    # Quarto 1
    cama1.render()
    wardrobe1.render()


    # Quarto 2
    cama2.render()
    wardrobe2.render()

    # Banheiro
    bathtub.render()
    toilet.render()
    sink.render()
    
    # Cubo de interação
    personagem.render()

    # Abajur().draw(0.7,{"x":-3,"y":-3,"z":1.45}) prefirimos não renderizar o abajur devido o LAG que causava :)
    glColor3f(1.0, 1.0, 1.0)
    glPopMatrix()

    pygame.display.set_caption('Projeto CASA - Computação Gráfica | FPS: %.2f' % clock.get_fps())
    pygame.display.flip()
