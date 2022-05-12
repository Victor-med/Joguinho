import pygame

pygame.init()

x = 250
y = 250
v = 20
vcomp = 15
vtiro = 30

xc = 100
yc = 100

yfum = y-1
xfum = x + 45
municao = 100

fonte = pygame.font.SysFont('Segoe UI bold', 25)
texto = fonte.render(f"Munição: {municao}", True, (0, 0, 0))
pos_texto = (20, 20)

carro = pygame.image.load("f1car.png")
pista = pygame.image.load("pista.png")
carro2 = pygame.image.load("f1carcomp.png")

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Guerra Formulaúnica')

atirar = False
window_opened = True
while window_opened:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_opened = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_w] and y >= 0:
        y -= v
    if comandos[pygame.K_a] and x >= 0:
        x -= v
    if comandos[pygame.K_s] and y <= 350:
        y += v
    if comandos[pygame.K_d] and x <= 400:
        x += v
    if comandos[pygame.K_p] and municao > 0:
        atirar = True
        recarga = False
        municao -= 1

    window.fill((0, 0, 0))
    window.blit(pista, (0,0))
    window.blit(carro, (x, y))
    window.blit(carro2, (xc, yc))
    window.blit(texto, pos_texto)
    if yc <= 500:
        yc += vcomp
    else:
        yc = 0

    if atirar:
        pygame.draw.circle(window, (255, 140, 0), (xfum, yfum), 5)

    if yfum >= 0:
        yfum -= vtiro
    else:
        atirar = False
        yfum = y-1
        xfum = x+45

    texto = fonte.render(f"Munição: {municao}", True, (0, 0, 0))
    pygame.display.update()

pygame.quit()
