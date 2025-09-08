import pygame, sys, time, random as rand 
from pygame.locals import *
#import numpy as np 


#initialize pygame engine 
pygame.init()

#create display surface
PIX_HEIGHT = 720
PIX_WIDTH = 720

DISPLAYSURF = pygame.display.set_mode((PIX_WIDTH, PIX_HEIGHT))

#define block/grid size
BLOCK = 10

#define FPS 
SPEED = 2
Clock = pygame.time.Clock()


#define colors
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)


#define snake
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        #initialize the snake as a rect obj, 4 blocks long 
        print("Initializing snake")
        #create empty starting lists for values 
        empt_list = [    [0, 0], 
                         [0, 0], 
                         [0, 0],  
                         [0, 0],  
                        ]  
        self.init_pos = empt_list
        self.pos = empt_list
        self.rect = empt_list
          
        #determine the initial position coordinates of the snake (4 blocks long) 
        self.init_pos = [[int(PIX_HEIGHT/2), int(PIX_WIDTH/2)], 
                         [int(PIX_HEIGHT/2), int(PIX_WIDTH/2) - BLOCK], 
                         [int(PIX_HEIGHT/2), int(PIX_WIDTH/2) - 2 * BLOCK],  
                         [int(PIX_HEIGHT/2), int(PIX_WIDTH/2) - 3 * BLOCK],  
                        ]
        #loop through coordinates to draw blocks representing snake, then draw the blocks
        for x in range(len(self.init_pos)):
            self.rect[x] = pygame.Rect(self.init_pos[x][0], self.init_pos[x][1],BLOCK,BLOCK)
            #draw the initial snake blocks
            pygame.draw.rect(DISPLAYSURF, WHITE, self.rect[x])

        
        #initial velocity [x, y]
        self.vel = ([0, 0]) 
        
    #track snakes position in an array, snake has pos(i) representing the length of the snake 
    #pos(1) = x, y, pos(2) = x,y, pos(3) = x, y 
    #snake structure is [[x, y]; [x, y]; [x, y]]
    def new_pos(self):
        #fill screen black to make the snake "move"
        DISPLAYSURF.fill((0, 0, 0))
        #get the initial position, use the velocity vector to update
        #first move the head
        self.pos[0] = [self.init_pos[0][0] + (self.vel[0] * BLOCK), 
                        #calculate new y coordinates
                        self.init_pos[0][1] + (self.vel[1] * BLOCK)]
        self.rect[0] = pygame.Rect(self.pos[0][0], self.pos[0][1], BLOCK,BLOCK)
        pygame.draw.rect(DISPLAYSURF, WHITE, self.rect[0])
        #move the body 
        for x in range(1, (len(self.init_pos))):
                        #calculate new x coordinates
            self.pos[x] = [self.init_pos[x][0], 
                        #calculate new y coordinates
                        self.init_pos[x][1]]  
            #calculate new cooordinates for rectanges 
            self.rect[x] = pygame.Rect(self.pos[x][0], self.pos[x][1], BLOCK,BLOCK)
            pygame.draw.rect(DISPLAYSURF, WHITE, self.rect[x])
        print("New Snake Pos:", self.pos)
        self.init_pos = self.pos

    def update(self):
        
        self.new_pos()
        
        
        

#spawn an apple at a random location on the grid 
def spawn_apple(): 
    #creat a rectangle 10x10 pixels
    rect = pygame.Rect(0, 0, BLOCK, BLOCK)
    
    #pick a random location in the window
    surf_size = DISPLAYSURF.get_size()

    #exclude all points within a 10 block radius of the snake
    appl_x = rand.randint(BLOCK*2,(surf_size[0]-(BLOCK*2)))
    appl_y = rand.randint(BLOCK*2,(surf_size[1]-(BLOCK*2)))
    rect.center = (appl_x, appl_y)
    
    #apple must be placed on the grid
    print("Spawning Apple at:",rect.center) 
    
    #draw the rectangle on the screen 
    pygame.draw.rect(DISPLAYSURF, RED, rect)

#count score, clear all apples
def eat_apple():
    #is snake on top of apple 
    #if snake on apple
        #spawn new apple 
        #return true 
    #elif 

    
    return False
    

#check user input and determine direction of snake 
def get_pressed_key():
    #creates array of user input 
    pressed_keys = pygame.key.get_pressed()

    #check if the following four keys have been pressed 
    if pressed_keys[K_LEFT]: 
        snake.vel = [-1,0]
    elif pressed_keys[K_RIGHT]:
        snake.vel = [1, 0]
    elif pressed_keys[K_UP]:
        snake.vel = [0, -1]
    elif pressed_keys[K_DOWN]:
        snake.vel = [0, 1]
    #else:
        #return [0,0]
    
def drawGrid():
    for x in range(0, PIX_WIDTH, BLOCK):
        for y in range(0, PIX_HEIGHT, BLOCK):
            rect = pygame.Rect(x, y, BLOCK, BLOCK)
            pygame.draw.rect(DISPLAYSURF, WHITE, rect, 1)
        
#Initialize snake
snake = Snake()

#for debug 
#drawGrid()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    Clock.tick(SPEED)
    pygame.display.update()
    #look for user input
    get_pressed_key()
    snake.update() 
    #spawn_apple()
    