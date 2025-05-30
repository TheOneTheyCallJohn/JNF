import random
import math

def neutronupdate(neutrons):
    ladder = []
    ladderx = []
    laddery = []
    for i in range(0,80):
        ladder.append(0)
        ladderx.append(0)
        laddery.append(0)
    for i in neutrons:
        ladderx[int(i[0][0]/2)+30] += 1
        laddery[int(i[0][1]/2)] += 1
        ladder[int(i[0][2]/20)] += 1
        i[0][0] += i[1][0]
        i[0][1] += i[1][1]
        i[0][2] += i[1][2]
        i[1][0] *= .999
        i[1][1] *= .999
        i[1][2] *= .999
        if random.randint(0,round(10000*(math.sqrt(i[1][0]**2+i[1][1]**2+i[1][2]**2) )        )) == 0:
            neutrons.remove(i)
            neutrons.append([[i[0][0],i[0][1],i[0][2]],[random.randint(-10,10)/10,random.randint(-10,10)/10,random.randint(-10,10)/10]])
            neutrons.append([[i[0][0],i[0][1],i[0][2]],[random.randint(-10,10)/10,random.randint(-10,10)/10,random.randint(-10,10)/10]])
            neutrons.append([[i[0][0],i[0][1],i[0][2]],[random.randint(-10,10)/10,random.randint(-10,10)/10,random.randint(-10,10)/10]])

        if i[0][0]+i[1][0] < -60 or i[0][0]+i[1][0] > 60:
            i[1][0] *= -1
        if i[0][1]+i[1][1] < -60 or i[0][1]+i[1][1] > 60:
            i[1][1] *= -1
        if i[0][2]+i[1][2] < 0 or i[0][2]+i[1][2] > 800:
            i[1][2] *= -1

    return neutrons, ladder, ladderx, laddery
    
def inobject(neut,importedstls):
    for i in importedstls:
        if (neut[0][0] > i[3][0][0]+i[1][0] and neut[0][0] < i[3][1][0]+i[1][0] and
        neut[0][1] > i[3][0][1]+i[1][1] and neut[0][1] < i[3][1][1]+i[1][1] and
        neut[0][2] > i[3][0][2]+i[1][2] and neut[0][2] < i[3][1][2]+i[1][2]): # Check to see if it's within the major bounds
            validfaces = []
            if math.sqrt((neut[0][0]-i[1][0])**2+(neut[0][1]-i[1][1])**2) < 5:
                return True, i[0][0]
            for j in range(len(i[2])): # Determine what faces are over the thing
                #print(" ")
                #print("Neutron      ",neut[0])
                #print("triangle   ",i[2][j][1])
                #print("vertex 0   ",i[2][j][1][0])
                #print("vertex 1   ",i[2][j][1][1])
                #print("vertex 2   ",i[2][j][1][2])
                #print("Min x      ", min(i[2][j][1][0][0], i[2][j][1][1][0], i[2][j][1][2][0]))
                #print("Neut X     ", neut[0][0], (neut[0][0] >= min(i[2][j][1][0][0], i[2][j][1][1][0], i[2][j][1][2][0]) 
                #and neut[0][0] <  max(i[2][j][1][0][0], i[2][j][1][1][0], i[2][j][1][2][0])))
                #print("Max x      ", max(i[2][j][1][0][0], i[2][j][1][1][0], i[2][j][1][2][0]))
                #print("Min y      ", min(i[2][j][1][0][1], i[2][j][1][1][1], i[2][j][1][2][1]))
                #print("Neut Y     ", neut[0][1], (neut[0][1] >= min(i[2][j][1][0][1], i[2][j][1][1][1], i[2][j][1][2][1]) 
                #and neut[0][1] <  max(i[2][j][1][0][1], i[2][j][1][1][1], i[2][j][1][2][1])))
                #print("Max y      ", max(i[2][j][1][0][1], i[2][j][1][1][1], i[2][j][1][2][1]))
                if (neut[0][0] >= min(i[2][j][1][0][0], i[2][j][1][1][0], i[2][j][1][2][0]) 
                and neut[0][0] <  max(i[2][j][1][0][0], i[2][j][1][1][0], i[2][j][1][2][0])
                and neut[0][1] >= min(i[2][j][1][0][2], i[2][j][1][1][2], i[2][j][1][2][2]) 
                and neut[0][1] <  max(i[2][j][1][0][2], i[2][j][1][1][2], i[2][j][1][2][2])):
                    #print("Penith    ",i[2][j][1])
                    #print(" ")
                    validfaces.append(i[2][j][1])
            #print(validfaces)
            #print(math.sqrt(neut[0][0]**2+neut[0][1]**2))

            if math.sqrt((neut[0][0]-i[1][0])**2+(neut[0][1]-i[1][1])**2) < 5:
                return True, i[0][0]
            greater = 0 
            for j in validfaces:
                if j[0][0] < neut[0][0]:
                    greater += 1
                    #return True
                
                    
            #print(len(validfaces))
            #print(validfaces)
    return False, 0
