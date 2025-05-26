import math
importedSTLS = []


def openfile(filename, Class, pos):
    filepath = filename
    newstl = [[len(importedSTLS)+1, Class, filename], pos, [],[[math.inf,math.inf,math.inf],[-math.inf,-math.inf,-math.inf]]]

    current_triangle = []
    with open(filepath, 'r') as file:
        for line in file:
            stripped = line.strip()
            if stripped.startswith("facet normal"):
                words = stripped.split()
                nx, ny, nz = float(words[2]), float(words[3]), float(words[4])
                #print(nx," ",ny," ", nz)
            if stripped.startswith("vertex"):
                words = stripped.split()
                x, y, z = float(words[1]), float(words[2]), float(words[3])
                if x > newstl[3][1][0]:
                    newstl[3][1][0] = x
                if x < newstl[3][0][0]:
                    newstl[3][0][0] = x
                if y > newstl[3][1][1]:
                    newstl[3][1][1] = y
                if y < newstl[3][0][1]:
                    newstl[3][0][1] = y
                if z > newstl[3][1][2]:
                    newstl[3][1][2] = z
                if z < newstl[3][0][2]:
                    newstl[3][0][2] = z
                current_triangle.append([x, y, z])
                if len(current_triangle) == 3:
                    
                    newstl[2].append([[nx,ny,nz],current_triangle])
                    current_triangle = []
    return newstl
    


def savefile(filename, importedSTLS):
    print("pee pee poo poo")


#print(importedSTLS)
