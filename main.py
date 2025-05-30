import pygame
import pygame_gui
from tkinter import Tk
from typing import List
from importer import openfile
from interactions import neutronupdate
from interactions import inobject
import math
pygame.init()
import random
from control import autocontrol
from control import manualcontrol
from control import controls
opfont = pygame.font.SysFont("candara", 15)
import pickle
rasin = 100
importedSTLS = []
neutrons = []
for i in range(0,10):
    for j in range(0,400):
        neutrons.append([[random.randint(-40,40),random.randint(-40,40),random.randint(0,200  )],[random.randint(-30,30)/10,random.randint(-30,30)/10,random.randint(-30,30)/10]])
# Settings
drawmode = "wireframe"
display_width = 1500
display_height = 750
framerate = 50
scale = .5
orgin = [display_width/2,550]
# Initialize
mdisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("John Nuclear Framework")
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((display_width, display_height))
Background = (125, 125, 125)
blue=(0,0,255)
lblue=(255,100,100)
rodsetpoint = 0
neutronsetpoint = 0
# State
running = True
counter = 0
menuoption = "Import STL"
labels = 0
autocontrola = -1
elementvis = []

# GUI Elements
#toggle_button = pygame_gui.elements.UIButton(
#    relative_rect=pygame.Rect((0, 30), (200, 50)),
#    text='Toggle Labels',
#    manager=manager
#)

dropdown = pygame_gui.elements.UIDropDownMenu(
    options_list=['File', 'Open', 'Save', 'Import STL'],
    starting_option='File',
    relative_rect=pygame.Rect((0, 0), (200, 30)),
    manager=manager
)

# Main loop
while running:
    time_delta = clock.tick(framerate) / 1000.0
    mdisplay.fill(Background)

    for event in pygame.event.get():
        manager.process_events(event)

        if event.type == pygame.QUIT:
            running = False

        # Keyboard control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                autocontrola *= -1
            if event.key == pygame.K_q:
                scale += .5
            if event.key == pygame.K_a:
                scale -= .5
            if autocontrola == 1:
                if event.key == pygame.K_w:
                    neutronsetpoint += 100
                if event.key == pygame.K_s:
                    neutronsetpoint -= 100
            if autocontrola == -1:
                if event.key == pygame.K_w:
                    rodsetpoint += 25
                if event.key == pygame.K_s:
                    rodsetpoint -= 25
            if event.key == pygame.K_e:
                orgin[1] += 50*scale
            if event.key == pygame.K_d:
                orgin[1] -= 50*scale*2


            if len(importedSTLS) > 4:
                if event.key == pygame.K_p:
                    rasin *= -1
                if event.key == pygame.K_f:
                    importedSTLS[0][1][2] += rasin
                if event.key == pygame.K_b:
                    importedSTLS[1][1][2] += rasin
                if event.key == pygame.K_t:
                    importedSTLS[2][1][2] += rasin
                if event.key == pygame.K_h:
                    importedSTLS[3][1][2] += rasin
                if event.key == pygame.K_v:
                    importedSTLS[4][1][2] += rasin
                if event.key == pygame.K_r:
                    importedSTLS[6][1][2] += rasin
                if event.key == pygame.K_n:
                    importedSTLS[7][1][2] += rasin
                if event.key == pygame.K_g:
                    importedSTLS[8][1][2] += rasin
                if event.key == pygame.K_y:
                    importedSTLS[10][1][2] += rasin



        # GUI events                
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == dropdown:
                menuoption = event.text
                print(f"Menu Selection: {menuoption}")  
                if menuoption == "Save":
                    
                    menuoption = "nothing"
                if menuoption == "Import STL":
                    file_path = "cylinder_10x800_ascii.stl"
      
                    test = openfile(len(importedSTLS),file_path, "Control Rod", [-50,0,0])
                    importedSTLS.append(test)     
                    test = openfile(len(importedSTLS),file_path, "Control Rod", [0,-50,0])
                    importedSTLS.append(test) 
                    test = openfile(len(importedSTLS),file_path, "Control Rod", [0,50,0])
                    importedSTLS.append(test) 
                    test = openfile(len(importedSTLS),file_path, "Control Rod", [50,0,0])
                    importedSTLS.append(test) 
                    test = openfile(len(importedSTLS),file_path, "Control Rod", [-35,-35,0])
                    importedSTLS.append(test) 
                    test = openfile(len(importedSTLS),file_path, "Neutron Detector", [-35/2,-35/2,0])
                    importedSTLS.append(test) 
                    test = openfile(len(importedSTLS),file_path, "Control Rod", [-35,35,0])
                    importedSTLS.append(test) 
                    test = openfile(len(importedSTLS),file_path, "Control Rod", [35,-35,0])
                    importedSTLS.append(test) 
                    test = openfile(len(importedSTLS),file_path, "Control Rod", [0,0,0])
                    importedSTLS.append(test)
                    test = openfile(len(importedSTLS),file_path, "Neutron Detector", [35/2,35/2,0])
                    importedSTLS.append(test)
                    test = openfile(len(importedSTLS),file_path, "Control Rod", [35,35,0])
                    importedSTLS.append(test)
                    test = openfile(len(importedSTLS),file_path, "Neutron Detector", [35/2,-35/2,0])
                    importedSTLS.append(test) 
                    test = openfile(len(importedSTLS),file_path, "Neutron Detector", [-35/2,35/2,0])
                    importedSTLS.append(test) 
 
                    file_path = "cylinder_120x800_ascii.stl"
                    #test = openfile(file_path, "Containment", [0,0,0])
                    #importedSTLS.append(test) 
    neutrons, ladder,ladderx,laddery = neutronupdate(neutrons)


    if autocontrola == 1:
        rodsetpoint = autocontrol(neutrons, importedSTLS, neutronsetpoint,rodsetpoint)
    elif autocontrola == -1:
        importedSTLS = manualcontrol(neutrons, importedSTLS,rodsetpoint)
    controls(autocontrola, rodsetpoint, neutronsetpoint, neutrons,importedSTLS,mdisplay)
        
    for i in importedSTLS:
        if i[0][1] == "Control Rod":
            if autocontrola == 1:
                i[1][2] = rodsetpoint
            drawmode = "solid"
        if i[0][1] == "Neutron Detector":
            drawmode = "solid"
            i[4][0].append(0)
            i[4][0].pop(0)
            #print(importedSTLS[ident][4][0])
        triangles = i[2]
        for triangle in triangles:
            normal, vertices = triangle

            v1, v2, v3 = vertices            
            def project(v):
                x = ((v[1] + i[1][1]) - (v[0] + i[1][0])) * scale + orgin[0]
                y = (((v[0] + i[1][0]) + (v[1] + i[1][1])) / 2 - (v[2] + i[1][2])) * scale + orgin[1]
                return (x, y)

            p1 = project(v1)
            p2 = project(v2)
            p3 = project(v3)
            nx, ny, nz = normal
            if i[0][1] == "Control Rod":
                color = (abs(nx)*255/6, abs(ny)*255/6, abs(nz)*255/6) 

            if i[0][1] == "Neutron Detector":
                color = (abs(nx)*255/12, abs(ny)*255/12, abs(nz)*255/12+100) 
            if (nx > 0 or ny > 0 or nz > 0): 
                if (drawmode == "solid"):
                    pygame.draw.polygon(mdisplay, color, [p1, p2, p3])   
                if (drawmode == "wireframe"):
                    pygame.draw.line(mdisplay, color, p1, p2)   
                    pygame.draw.line(mdisplay, color, p3, p2)
                    pygame.draw.line(mdisplay, color, p3, p1)
    
    
    for i in neutrons:
        #print("hi")
        testtt, ident = inobject(i,importedSTLS) 
        #print(testtt)
        if testtt == True:
            if importedSTLS[ident][0][1] == "Control Rod":
                color = lblue
                neutrons.remove(i)
            if importedSTLS[ident][0][1] == "Neutron Detector":
                if random.randint(1,100) == 1:
                    neutrons.remove(i)
                #print("FR", importedSTLS[ident][4][0])
                importedSTLS[ident][4][0][len(importedSTLS[ident][4][0])-1] += 1
                color = (0,255,255)
                
        if testtt == False:
            color = blue
        x = (i[0][1] - i[0][0]) * scale + orgin[0]
        y = ((i[0][0] + i[0][1]) / 2 - i[0][2]) * scale + orgin[1]
        #print(x)
        #print(y)
        pygame.draw.circle(mdisplay, color, (x,y), 2)
                #pygame.draw.circle(mdisplay, (0,0,255), (i[0],i[1]), 2)
    x = (100 - 0) * scale + orgin[0]
    ox = (-100 - 0) * scale + orgin[0]
    y = ((0 + 100) / 2 ) * scale + orgin[1]
    oy = ((0 - 0) / 2  - 800) * scale + orgin[1]
    pygame.draw.line(mdisplay,(0,255,0),(orgin[0],orgin[1]),(x,y),2)
    pygame.draw.line(mdisplay,(255,0,0),(orgin[0],orgin[1]),(ox,y),2)
    pygame.draw.line(mdisplay,(0,0,255),(orgin[0],orgin[1]),(orgin[0],oy),2)
    period = 0
    mdisplay.blit(opfont.render(f"Neuton Count: {len(neutrons)} Rod Setpoint: {rodsetpoint} Neutron Setpoint: {neutronsetpoint} True peroid{period}", 1, (255,255,225)),(200, 10))


    for i in range(0,len(ladder)):
        pygame.draw.line(mdisplay,(0,0,255),(display_width-10,750-i*10),(display_width-10-ladder[i]*5,750-i*10),2)
    for i in range(0,len(ladderx)):
        pygame.draw.line(mdisplay,(255,0,0),(display_width-10-i*10,10),(display_width-10-i*10,10+ladderx[i]*5),2)
    #for i in range(0,len(laddery)):
        #pygame.draw.line(mdisplay,(0,255,0),(display_width-10-i*10,10),(display_width-10-ladder[i]*5,750-i*10),2)
        
    elementvis =[]
    #for i in range(len(importedSTLS)):
        #button = pygame_gui.elements.UIButton(
        #relative_rect=pygame.Rect((50, 50+i*50), (150, 50+i*50)),
        #text='Click Me',
        #manager=manager)
        #elementvis.append(button)



    manager.update(time_delta)
    manager.draw_ui(mdisplay)
    pygame.display.update()

pygame.quit()
