import pygame

LARGURA = 600
ALTURA = 385

g = 25.807

aceleracao_x = 0
aceleracao_y = 0

posx_mario = 0
posy_mario = 238

posx_cano = 300
posy_cano = 205
vcano = -10

posx_canolongo = 800
posy_canolongo = 58
vcanolongo = -10

tempo = pygame.time.Clock()

tempos = 0
vpulo = -12.5
altura_mario = posy_mario

pygame.font.init()
FONTE = pygame.font.SysFont('arial', 50)

pygame.init()

pygame.mixer.music.load('toque.mp3')

mario = pygame.image.load('mario.png')
fundo = pygame.image.load('backfundo.png')
cano = pygame.image.load('cano.png')
canolongo = pygame.image.load('canolongo.png')

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Mario fake')

window_opened = True
pygame.mixer.music.play(-1)
while window_opened:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_opened = False

    comando = pygame.key.get_pressed()
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
        aceleracao_y = -27
        posy_mario += aceleracao_y

    if posx_cano > -50:
        posx_cano += vcano
    else:
        posx_cano = 900

    if posx_canolongo > -50:
        posx_canolongo += vcanolongo
    else:
        posx_canolongo = 900

    window.fill((0, 0, 0))

    T = tempo.get_time() / 1000
    f = g * T
    aceleracao_y += f
    posy_mario += aceleracao_y

    if posy_mario > 238:
        posy_mario = 238
        aceleracao_y = 0
        tempo = pygame.time.Clock()

    if (posx_mario + 50 > posx_cano) and (posy_mario + 50 > posy_cano):
        posx_mario = 0

    if (posx_mario + 50 > posx_canolongo) and (posy_mario + 50 > posy_canolongo):
        posx_mario = 0


    window.blit(fundo, (0,0))
    mario_w = window.blit(mario, (posx_mario, posy_mario))
    cano_w = window.blit(cano, (posx_cano, posy_cano))
    canolongo_w = window.blit(canolongo, (posx_canolongo, posy_canolongo))
    pygame.display.update()
    tempo.tick(1000)

pygame.quit()