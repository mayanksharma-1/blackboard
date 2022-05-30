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
    pygame.draw.rect(screen,'gray',[0,0,50,HEIGHT]) #(x,y,w,h)  top left coordinates (x,y) width and height (w,h) 
    pygame.draw.line(screen,'black',[50,0],[50,HEIGHT],2)
    brush = pygame.draw.rect(screen,'black',[10,10,30,30]) 
    brush_circle = pygame.draw.circle(screen,'white',(25,25),7.5)

run = True
while run:
    timer.tick(fps)
    screen.fill((255,255,255)) #white 
    
    draw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
    #print(pygame.mouse.get_pos())

pygame.quit()