from matplotlib.pyplot import draw
import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 1300
HEIGHT = 600

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Painting Tool')

def draw_window():
    pygame.draw.rect(screen,'gray',[0,0,70,HEIGHT])

run = True
while run:
    timer.tick(fps)
    screen.fill((255,255,255)) #white 
    
    draw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()