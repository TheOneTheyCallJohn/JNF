import pygame
from UIelements import dial
from UIelements import light
raisin = -100
neutroncount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def autocontrol(neutrons,importedSTLs, neutronsetpoint,rodsetpoint):
    neutroncount.pop(0)
    neutroncount.append(len(neutrons))
    rateofchange = neutroncount[len(neutroncount)-1]-neutroncount[len(neutroncount)-51]
    setrateofchange = (neutronsetpoint - len(neutrons))
    
    if  len(neutrons) < neutronsetpoint:
        if rateofchange < (neutronsetpoint-len(neutrons))/10:
            rodsetpoint += .1
        elif rateofchange > (neutronsetpoint-len(neutrons))/10:
            rodsetpoint -= .1
    if  len(neutrons) > neutronsetpoint:
        if rateofchange < (neutronsetpoint-len(neutrons))/10:
            rodsetpoint += .1
        elif rateofchange > (neutronsetpoint-len(neutrons))/10:
            rodsetpoint -= .1
    return rodsetpoint
    
    
    
def manualcontrol(neutrons,importedSTLS,rodsetpoint):
    
    return importedSTLS
    for event in pygame.event.get():

        # Keyboard control
        if event.type == pygame.KEYDOWN:
            if len(importedSTLS) > 4:
                if event.key == pygame.K_p:
                    raisin *= -1
                if event.key == pygame.K_r:
                    importedSTLS[1][1][2] += rasin
                if event.key == pygame.K_t:
                    importedSTLS[2][1][2] += rasin
                if event.key == pygame.K_y:
                    importedSTLS[3][1][2] += rasin
                if event.key == pygame.K_f:
                    importedSTLS[4][1][2] += rasin
                if event.key == pygame.K_g:
                    importedSTLS[5][1][2] += rasin
                if event.key == pygame.K_h:
                    importedSTLS[6][1][2] += rasin
                if event.key == pygame.K_v:
                    importedSTLS[7][1][2] += rasin
                if event.key == pygame.K_b:
                    importedSTLS[8][1][2] += rasin
                if event.key == pygame.K_n:
                    importedSTLS[9][1][2] += rasin
    
    
    
    return importedSTLS

def controls(autocontrol, rodsetpoint, neutronsetpoint, neutrons,importedSTLs, mdisplay):
    dial(100,100,50,len(neutrons),True,mdisplay, "Neutron Count",(0,255,0))
    dial(250,100,50,rodsetpoint/8*3,True,mdisplay, "Rod Position",(0,255,0))
    NDs = []
    CRs = []
    for i in importedSTLs:
        if i[0][1] == "Neutron Detector":
            NDs.append(i[0][0])
        if i[0][1] == "Control Rod":
            CRs.append(i[0][0])
    #print(NDs)
    for i in range(0,len(CRs)):
        dial(importedSTLs[CRs[i]][1][0]*3+400,-importedSTLs[CRs[i]][1][1]*3+400,20,importedSTLs[CRs[i]][1][2]/800*360,True,mdisplay, f"CR{importedSTLs[CRs[i]][1][1],importedSTLs[CRs[i]][1][0]}",(255,0,0))
    for i in range(0,len(NDs)):
        #print(importedSTLs[NDs[i]][4][0][0])
        dial(importedSTLs[NDs[i]][1][0]*3+400,-importedSTLs[NDs[i]][1][1]*3+400,20,sum(importedSTLs[NDs[i]][4][0])/10,True,mdisplay, f"ND{importedSTLs[CRs[i]][1][1],importedSTLs[CRs[i]][1][0]}",(0,0,255))

    
    light(400,100,(255,0,0), 10, len(neutrons) - 300 > neutronsetpoint, mdisplay, "High Activity")
    light(400,120,(0,0,255), 10, len(neutrons) + 300 < neutronsetpoint, mdisplay, "Low Activity")
    light(400,140,(0,255,0), 10, autocontrol == 1, mdisplay, "Autocontrol")
