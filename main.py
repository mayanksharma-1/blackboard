import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 1600
HEIGHT = 900

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Painting Tool')

run = True
while run:
    timer.tick(fps)
    screen.fill((255,255,255)) #white 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()