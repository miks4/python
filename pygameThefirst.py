import pygame
import os.path


#inicijalizacija pygame-a
pygame.init()




screen = pygame.display.set_mode((600,300))#x i y osa
myfont = pygame.font.SysFont("Arial", 60,)
label = myfont.render("hello world" ,1, (255,255,0))#rgb
clock = pygame.time.Clock()
FPS = 30
filepath = os.path.dirname(__file__)
pygame.display.set_caption("SNAKE - GAME")
icon = pygame.image.load(os.path.join(filepath, 'snake.png'))
pygame.display.set_icon(icon)


#playerImg = pygame.image.load('snake.png')
#plyerX = 370
#playerY = 150

def player():
    screen.blit(playerImg,(plyerX,playerY))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    #player()
    screen.blit(label,(100,100))
    pygame.display.update()
    clock.tick(FPS)

