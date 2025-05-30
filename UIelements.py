import pygame
import math
opfont = pygame.font.SysFont("candara", 15)


def dial(x,y,size,angle,showvalue, mdisplay, label, color):
    pygame.draw.line(mdisplay,color,(x,y),(x+size*-math.cos(angle*3.14/180),y+size*-math.sin(angle*3.14/180)),2)
    pygame.draw.circle(mdisplay,color,(x,y),size,2)
    mdisplay.blit(opfont.render(label, 1, (0,0,0)),(x -30, y+size ))

def light(x,y,color, size, on, mdisplay, label):
    if on == True:
        pygame.draw.circle(mdisplay,color,(x,y),size,size)
    pygame.draw.circle(mdisplay,(0,0,0),(x,y),size,1)
    mdisplay.blit(opfont.render(label, 1, (0,0,0)),(x + size, y-5 ))

#def buttons(x,y,color,size,mdisplay,label,bid):
    #pygame.draw.rect(mdisplay,(color),) 