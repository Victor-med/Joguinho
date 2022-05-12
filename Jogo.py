import pygame

pygame.init()

window = pygame.display.set_mode((1000,500))
pygame.display.set_caption('Ataque dos zumbis')

jogador = pygame.image.load('normal.png')
teste = pygame.image.load('andando.gif')

x = 0
y = 400
v = 10
vmax = 12

pulo = False
window_opened = True
while window_opened:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_opened = False

    comando = pygame.key.get_pressed()
    if comando[pygame.K_a]:
        jogador = pygame.image.load('atirando.png')
    if comando[pygame.K_RIGHT]:
        x += v
        jogador = pygame.image.load('normal.png')
    if comando[pygame.K_LEFT]:
        x -= v
        jogador = pygame.image.load('normal-l.png')
    if comando[pygame.K_LEFT] and comando[pygame.K_c]:
        x -= vmax
        jogador = pygame.image.load('correndo-l.png')
    if comando[pygame.K_RIGHT] and comando[pygame.K_c]:
        x += vmax
        jogador = pygame.image.load('correndo-d.png')
    #if comando[pygame.K_SPACE]:
      #  pulo = True
       # jogador = pygame.image.load('pula.png')
       # if y >= 340:
        #    y -=30
       # else:
         #   y = 400

    window.fill((0,0,0))
    window.blit(jogador, (x, y))

    pygame.display.update()

pygame.quit()