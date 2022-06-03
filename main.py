from matplotlib.pyplot import draw
import pygame 
import os
pygame.init()

fps = 120
timer = pygame.time.Clock()
WIDTH = 1300
HEIGHT = 600
CHALK_SIZE = 0
DRAWING = []
CHALK_IMAGE = pygame.image.load(os.path.join("assets","chalk.svg"))
CHALK_IMAGE = pygame.transform.scale(CHALK_IMAGE,(20,70))

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('BlackBoard')

def draw_window(CHALK_IMAGE):
    pygame.draw.rect(screen,'gray',[0,0,50,HEIGHT]) #(x,y,w,h)  top left coordinates (x,y) width and height (w,h) 
    #pygame.draw.line(screen,'white',[50,0],[50,HEIGHT],2)
    #chalk = pygame.draw.rect(screen,'black',[10,10,30,30]) 
    chalk = screen.blit(CHALK_IMAGE,(10,10))

    chalk_size = 7.5
    #chalk_circle = pygame.draw.circle(screen,'white',(25,25),chalk_size)

    

    return chalk
def drawing():
    for i in range(len(DRAWING)):
        pygame.draw.circle(screen,'white',DRAWING[i][1],DRAWING[i][0]) # DRAWING[i][1] = the mouse value ; DRAWING[i][0] = the CHALK_SIZE



run = True
while run:
    timer.tick(fps)
    screen.fill('black')  
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    if mouse[0] > 50:
        pygame.draw.circle(screen,'white',mouse,CHALK_SIZE)
    chalk = draw_window(CHALK_IMAGE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if chalk.collidepoint(event.pos):
                CHALK_SIZE = 7.5
    if click and mouse[0] > 70:
        DRAWING.append((CHALK_SIZE,mouse))
    drawing()

    
    pygame.display.flip()
    #print(pygame.mouse.get_pos())

pygame.quit()