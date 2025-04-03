import pygame, sys, time, random as rand 
from pygame.locals import *


#initialize pygame engine 
pygame.init()

#create display surface
DISPLAYSURF = pygame.display.set_mode((720, 720))
#define block size
BLOCK = 10
#define FPS 
FPS = pygame.time.Clock()
FPS.tick(30)

#define colors
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

#define snake
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        #initialize the snake as a rect obj
        print("Initializing snake")
        self.rect = pygame.Rect(0,0,BLOCK,BLOCK)
        pygame.draw.rect(DISPLAYSURF, WHITE, self)
    
    #new position will move by one block in a single direction
    def calcnewpos(self):
        #pygame.self.move(BLOCK,BLOCK)
        

    #def update(self):
        #print("Update Snake")
        #self.calcnewpos() test
    

#spawn an apple at a random location 
def spawn_apple(): 
    #creat a rectangle 10x10 pixels
    rect = pygame.Rect(0, 0, BLOCK, BLOCK)
    
    #pick a random location in the window
    surf_size = DISPLAYSURF.get_size()

    #exclude all points within a 10 block radius of the snake
    x_rand = rand.randint(BLOCK*2,(surf_size[0]-(BLOCK*2)))
    y_rand = rand.randint(BLOCK*2,(surf_size[1]-(BLOCK*2)))
    rect.center = (x_rand, y_rand)
    
    print("Spawning Apple at:",rect.center) 
    
    #draw the rectangle on the screen 
    pygame.draw.rect(DISPLAYSURF, RED, rect)

#count score, clear all apples
def eat_apple():
    print("spawning new apple")

#check user input
def get_pressed_key():
    #creates array of user input 
    pressed_keys = pygame.key.get_pressed()
    
    #check if the following four keys have been pressed 
    if pressed_keys[K_LEFT]: 
        print("move left")
        
    elif pressed_keys[K_RIGHT]: 
        print("move right")

    elif pressed_keys[K_UP]:
        print("move up")
        
    elif pressed_keys[K_DOWN]: 
        print("move down") 
        
#Initialize snake
snake = Snake()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    
    #look for user input
    snake.update()
    get_pressed_key()
    spawn_apple()
    time.sleep(1)

    