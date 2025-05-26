import pygame
import pygame_gui
from tkinter import Tk
from typing import List
from importer import openfile
from interactions import neutronupdate
from interactions import inobject
import math
pygame.init()




importedSTLS = []
neutrons = []
for i in range(-10,10):
    for j in range(-10,10):
        neutrons.append([[i,j,50],[0.01*5,-0.005*5,0]])
# Settings
drawmode = "solid"
display_width = 1500
display_height = 750
framerate = 50
scale = 5
orgin = [550,550]
# Initialize
mdisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("John Nuclear Framework")
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((display_width, display_height))
Background = (125, 125, 125)
blue=(0,0,255)
lblue=(255,100,100)

# State
running = True
counter = 0
menuoption = "nothing"
labels = 0

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
            if event.key == pygame.K_q:
                scale += .5
            if event.key == pygame.K_a:
                scale -= .5


            if event.key == pygame.K_e:
                orgin[1] += 10
            if event.key == pygame.K_d:
                orgin[1] -= 10

        # GUI events                
        if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == dropdown:
                menuoption = event.text
                print(f"Menu Selection: {menuoption}")  
                if menuoption == "Import STL":
                    file_path = "cylinder_10x800_ascii.stl"
      
                    test = openfile(file_path, "Control Rod", [50,0,0])
                    importedSTLS.append(test)     
                    test = openfile(file_path, "Control Rod", [-50,0,0])
                    importedSTLS.append(test) 
                    test = openfile(file_path, "Control Rod", [0,50,0])
                    importedSTLS.append(test) 
                    test = openfile(file_path, "Control Rod", [0,-50,0])
                    importedSTLS.append(test) 
                    test = openfile(file_path, "Control Rod", [-35,-35,0])
                    importedSTLS.append(test) 
                    test = openfile(file_path, "Control Rod", [-35,35,0])
                    importedSTLS.append(test) 
                    test = openfile(file_path, "Control Rod", [35,-35,0])
                    importedSTLS.append(test) 
                    test = openfile(file_path, "Control Rod", [0,0,0])
                    importedSTLS.append(test)
                    test = openfile(file_path, "Control Rod", [35,35,0])
                    importedSTLS.append(test) 
    neutrons = neutronupdate(neutrons)





    for i in importedSTLS:

        triangles = i[2]
        for triangle in triangles:
            normal, vertices = triangle

            # Extract vertices
            v1, v2, v3 = vertices
            
            # Convert 3D to 2D (simple projection)
            def project(v):
                x = ((v[1] + i[1][1]) - (v[0] + i[1][0])) * scale + orgin[0]
                y = (((v[0] + i[1][0]) + (v[1] + i[1][1])) / 2 - (v[2] + i[1][2])) * scale + orgin[1]
                return (x, y)

            p1 = project(v1)
            p2 = project(v2)
            p3 = project(v3)
            nx, ny, nz = normal

            color = (abs(nx)*255/6, abs(ny)*255/6, abs(nz)*255/6) 
            if (nx > 0 or ny > 0 or nz > 0): 
                if (drawmode == "solid"):
                    pygame.draw.polygon(mdisplay, color, [p1, p2, p3])   
                if (drawmode == "wireframe"):
                    pygame.draw.line(mdisplay, color, p1, p2)   
                    pygame.draw.line(mdisplay, color, p3, p2)
                    pygame.draw.line(mdisplay, color, p3, p1)

    for i in neutrons:
        #print("hi")
        testtt = inobject(i,importedSTLS) 
        #print(testtt)
        if testtt == True:
            color = lblue
        if testtt == False:
            color = blue
        x = (i[0][1] - i[0][0]) * scale + orgin[0]
        y = ((i[0][0] + i[0][1]) / 2 - i[0][2]) * scale + orgin[1]
        #print(x)
        #print(y)
        pygame.draw.circle(mdisplay, color, (x,y), 2)
                #pygame.draw.circle(mdisplay, (0,0,255), (i[0],i[1]), 2)
    
    manager.update(time_delta)
    manager.draw_ui(mdisplay)
    pygame.display.update()

pygame.quit()
