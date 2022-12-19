import pygame
from pygame import mixer

pygame.init()

width = 1400   # 16:9
height = 800   # 16:9


black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Beat Maker")
label_font = pygame.font.SysFont("./assets/Roboto-Bold.ttf", 32)

fps = 60
timer = pygame.time.Clock()
beats = 8
intruments = 6

def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, height - 200], 5)
    bottom_box = pygame.draw.rect(
        screen, gray, [0, height - 200, width, 200], 5)
    boxes = []
    colors = [gray, white, gray]

    # Labels
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 40))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 140))
    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (30, 240))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30, 340))
    clap_text = label_font.render('Clap', True, white)
    screen.blit(clap_text, (30, 440))
    tom_text = label_font.render('Floor Tom', True, white)
    screen.blit(tom_text, (30, 540))

    # Boxes
    for i in range(6):
        pygame.draw.line(
            screen, gray, [0, (100 * i) + 100], [width, (i*100) + 100], 5)
    for i in range(beats):
        for j in range(intruments):
            rect = pygame.draw.rect(
                screen, 
                gray, 
                [
                    i * (width - 200) // beats + 200, 
                    (j * 100) , 
                    (width - 200) // beats, 
                    (height - 200) // intruments
                ], 
                5
                )

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
