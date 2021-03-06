import pygame
import random

LARGURA = 600
ALTURA = 385

g = 0

velocidade_y = 0
aceleracao_y = 0

posx_mario = 0
posy_mario = 0

posx_cano = 0
posy_cano = 0
vcano = 0

tempo = pygame.time.Clock()

pygame.font.init()

pygame.init()

pygame.mixer.music.load('toque.mp3')

mario = pygame.image.load('mario.png')
fundo = pygame.image.load('backfundo.png')
cano = pygame.image.load('canolongo.png')

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Mario fake')


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    window.blit(texto1, (x, y))

def start_cano():
    global posx_cano
    global posy_cano
    posx_cano = 550
    posy_cano = random.randint(58, 230)


def init_game():
    global g
    g = 25.807
    
    global velocidade_y
    global aceleracao_y
    velocidade_y = 0
    aceleracao_y = 0

    global posx_mario
    global posy_mario
    posx_mario = 0
    posy_mario = 238
    
    global posx_cano
    global posy_cano
    global vcano
    start_cano()
    vcano = -10

    global tempo
    tempo = pygame.time.Clock()


def morreu():
    global posx_mario
    posx_mario = 0
    window.blit(fundo, (0, 0))
    texto('Morreu playboy', (255, 140, 0), 50, 150, 100)
    pygame.display.update()
    pygame.time.delay(3000)
    init_game()



def colisao():
    global posx_mario
    global posy_mario
    global posx_cano
    global posy_cano

    if (posx_mario + 40 > posx_cano) and (posy_mario + 50 > posy_cano) and (posx_mario < posx_cano + 40):
        morreu()
    if (posx_mario < posx_cano + 110) and (posy_mario + 50 > posy_cano) and (posx_mario + 40 > posx_cano):
        morreu()


def movimentos(comando):
    global posx_mario
    global posy_mario
    global velocidade_y
    global aceleracao_y
    global mario
    if comando[pygame.K_RIGHT] and posx_mario <= 510:
        posx_mario += 15
        mario = pygame.image.load('mario.png')
    if comando[pygame.K_LEFT] and posx_mario >= 0:
        posx_mario -= 15
        mario = pygame.image.load('mario-left.png')
    if comando[pygame.K_RIGHT] and comando[pygame.K_t] and posx_mario <= 510:
        posx_mario += 20
        mario = pygame.image.load('mario.png')
    if comando[pygame.K_t] and comando[pygame.K_LEFT] and posx_mario >= 0:
        posx_mario -= 20
        mario = pygame.image.load('mario-left.png')
    if comando[pygame.K_UP] and posy_mario == 238:
        velocidade_y -= 32
        posy_mario += velocidade_y


init_game()

window_opened = True
pygame.mixer.music.play(-1)
while window_opened:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_opened = False

    movimentos(pygame.key.get_pressed())

    if posx_cano > -110:
        posx_cano += vcano
    else:
        start_cano()

    # window.fill((0, 0, 0))

    aceleracao_y += g/100
    velocidade_y += aceleracao_y
    posy_mario += velocidade_y

    if posy_mario > 238:
        posy_mario = 238
        velocidade_y = 0
        aceleracao_y = 0
        tempo = pygame.time.Clock()

    colisao()

    window.blit(fundo, (0, 0))
    mario_w = window.blit(mario, (posx_mario, posy_mario))
    cano_w = window.blit(cano, (posx_cano, posy_cano))
    pygame.display.update()
    tempo.tick(1000)

pygame.quit()
