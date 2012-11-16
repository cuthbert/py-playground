import sys, pygame, random

random.seed
pygame.init()

screenSize = width, height = 640, 480
tileSize = tileWidth, tileHeight = 32, 32
grid = gridWidth, gridHeight = width/tileWidth, height/tileHeight

worldSize = worldWidth, worldHeight = 64,gridHeight


def createTileRect(x,y=None): 
    if (type(x)==tuple):
        return pygame.Rect(x[0]*tileWidth, x[1]*tileHeight,tileWidth,tileHeight)
    return pygame.Rect(x*tileWidth, y*tileHeight,tileWidth,tileHeight) 


tiles = {
        "Stone": (1,0),
        "Bedrock": (1,1),
        "Diamond": (2,3)
}

speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(screenSize)

terrainImg = pygame.image.load("terrain.png").convert()

world = pygame.Surface((tileWidth*worldWidth, tileHeight*worldHeight))

#create surfaceMap
surfaceMap = [] #TODO: cleverer array initialization; python can do
for i in range(0, worldWidth):
    tempCol = []
    for j in range(0, worldHeight):  
        tempCol.append(None)
    surfaceMap.append(tempCol)


for i in range(0, worldWidth):
    
    r = random.randint(0,9)
            
    if(r<=5):
        surfaceMap[i][worldHeight-2] = tiles["Bedrock"]
    elif r<=8:
        surfaceMap[i][worldHeight-2] = tiles["Stone"]
    else:
        surfaceMap[i][worldHeight-2] = tiles["Diamond"]
    
    surfaceMap[i][worldHeight-1] = tiles["Bedrock"] 
    
for i in range(0, worldWidth):
    for j in range(0, worldHeight):
        if (surfaceMap[i][j]==None):
            continue
        world.blit(terrainImg, createTileRect(i, j), createTileRect(surfaceMap[i][j]))
    




frames = 0
posx = 0
oldPosx = -1
keytime = 0
while 1:
    time = pygame.time.get_ticks()
    
    frames=frames+1
    fps = frames/float(time)*1000
    print fps
        
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F4|pygame.KMOD_ALT: sys.exit()

    #check keys
    keys = pygame.key.get_pressed()
    if time-keytime>100:
        keytime = time
        if keys[pygame.K_RIGHT] and posx<worldWidth-gridWidth:
            posx+=1
        elif keys[pygame.K_LEFT] and posx>0:
            posx-=1

    #drawing
    
    if posx!=oldPosx:
        screen.fill(black)
        #print str(posx)+" "+str(oldPosx)
        screen.blit(world, (0,0), (posx*tileWidth, 0, (posx+gridWidth)*tileWidth-1, (worldHeight*tileHeight)))
    
    pygame.display.flip()
    
    pygame.time.delay(10)
    oldPosx = posx
