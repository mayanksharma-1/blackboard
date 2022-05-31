from matplotlib.pyplot import draw
import pygame
pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 1300
HEIGHT = 600
BRUSH_SIZE = 0
DRAWING = []

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Painting Tool')

def draw_window():
    pygame.draw.rect(screen,'gray',[0,0,50,HEIGHT]) #(x,y,w,h)  top left coordinates (x,y) width and height (w,h) 
    pygame.draw.line(screen,'black',[50,0],[50,HEIGHT],2)
    brush = pygame.draw.rect(screen,'black',[10,10,30,30]) 
    brush_size = 7.5
    brush_circle = pygame.draw.circle(screen,'white',(25,25),7.5)

    return brush
def draw():
    for i in range(len(DRAWING)):
        pygame.draw.circle(screen,'black',DRAWING[i][1],DRAWING[i][0]) # DRAWING[i][1] = the mouse value ; DRAWING[i][0] = the BRUSH_SIZE



run = True
while run:
    timer.tick(fps)
    screen.fill((255,255,255)) #white 
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    if mouse[0] > 50:
        pygame.draw.circle(screen,'black',mouse,BRUSH_SIZE)
    brush = draw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if brush.collidepoint(event.pos):
                BRUSH_SIZE = 7.5
    if click and mouse[0] > 70:
        DRAWING.append((BRUSH_SIZE,mouse))
    draw()

    
    pygame.display.flip()
    #print(pygame.mouse.get_pos())

pygame.quit()