'''
Created on 16.11.2012

@author: cuthbert
'''

import sys, pygame, random

class Game(object):
    def __init__(self):                
        self.screenSize = self.width, self.height = 640, 640
        self.tileSize = self.tileWidth, self.tileHeight = 32, 32
        self.grid = self.gridWidth, self.gridHeight = self.width/self.tileWidth, self.height/self.tileHeight
        
        self.worldSize = self.worldWidth, self.worldHeight = 64,self.gridHeight
        
        
        self.tiles = {
                "Stone": (1,0),
                "Dirt": (2,0),
                "Bedrock": (1,1),
                "Diamond": (2,3),
                "Broke1": (0,15),
                "Flower": (12,0)
        }
        
    def run(self):
        random.seed
        pygame.init()
        
        screen = pygame.display.set_mode(self.screenSize)
        
        terrainImg = pygame.image.load("terrain.png").convert_alpha()
        
        world = pygame.Surface((self.tileWidth*self.worldWidth, self.tileHeight*self.worldHeight))
        world.fill((0,0,128))
        
        #create surfaceMap
        surfaceMap = [] #TODO: cleverer array initialization; python can do
        for i in range(0, self.worldWidth):
            tempCol = []
            for j in range(0, self.worldHeight):  
                tempCol.append(None)
            surfaceMap.append(tempCol)
        
        
        for i in range(0, self.worldWidth):
            for j in range(0, self.worldHeight):
                if (j<self.worldHeight/2):
                    surfaceMap[i][j] = self.tiles["Broke1"]
                elif (j>=self.worldHeight/2 and j<self.worldHeight/4*3):
                    surfaceMap[i][j] = self.tiles["Dirt"]
                elif (j>=self.worldHeight/4*3 and j<self.worldHeight-2):
                    surfaceMap[i][j] = self.tiles["Stone"]
                elif (j==self.worldHeight-2):
                    r = random.randint(0,9)
                    if(r<=5):
                        surfaceMap[i][j] = self.tiles["Bedrock"]
                    elif r<=8:
                        surfaceMap[i][j] = self.tiles["Stone"]
                    else:
                        surfaceMap[i][j] = self.tiles["Diamond"]
                else:
                    surfaceMap[i][j] = self.tiles["Bedrock"] 
            
        for i in range(0, self.worldWidth):
            for j in range(0, self.worldHeight):
                if (surfaceMap[i][j]==None):
                    continue
                world.blit(terrainImg, self.createTileRect(i, j), self.createTileRect(surfaceMap[i][j]))
                r=random.randint(0,9)
                if r==0:
                    world.blit(terrainImg, self.createTileRect(i, j), self.createTileRect(self.tiles["Flower"]))
        
        
        
        
        frames = 0
        posx = 0
        posy = 0
        oldPosx = -1
        oldPosy = -1
        keytime = 0
        while 1:
            time = pygame.time.get_ticks()
            
            frames=frames+1
            fps = frames/float(time)*1000
            #print fps
                
            #event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F4|pygame.KMOD_ALT: sys.exit()
        
            #check keys
            keys = pygame.key.get_pressed()
            if time-keytime>100:
                keytime = time
                if keys[pygame.K_RIGHT] and posx<self.worldWidth-self.gridWidth:
                    posx+=1
                elif keys[pygame.K_LEFT] and posx>0:
                    posx-=1
                if keys[pygame.K_DOWN] and posy<self.worldHeight-self.gridHeight:
                    posy+=1
                elif keys[pygame.K_UP] and posy>0:
                    posy-=1
        
            #drawing
            
            if posx!=oldPosx or posy!=oldPosy:
                #print str(posx)+" "+str(oldPosx)
                screen.blit(world, (0,0), (posx*self.tileWidth, posy*self.tileHeight, (posx+self.gridWidth)*self.tileWidth-1, (posy+self.gridHeight)*self.tileHeight-1))
            
            pygame.display.flip()
            
            #pygame.time.delay(10)
            oldPosx = posx
            oldPosy = posy
        
    def createTileRect(self, x,y=None): 
        if (type(x)==tuple):
            return pygame.Rect(x[0]*self.tileWidth, x[1]*self.tileHeight,self.tileWidth,self.tileHeight)
        return pygame.Rect(x*self.tileWidth, y*self.tileHeight,self.tileWidth,self.tileHeight) 
        
        