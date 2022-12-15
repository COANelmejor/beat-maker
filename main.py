import pygame
from pygame import mixer

pygame.init()

width = 800
height = 600

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Beat Maker")
label = pygame.font.SysFont("./assets/Roboto-Bold.ttf", 32)

fps = 60
timer = pygame.time.Clock()

run = True
while run:
    timer.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()