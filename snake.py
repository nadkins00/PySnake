import pygame, sys, time, random as rand 
from pygame.locals import *


#initialize pygame engine 
pygame.init()

#create display surface
PIX_HEIGHT = 720
PIX_WIDTH = 720

DISPLAYSURF = pygame.display.set_mode((PIX_WIDTH, PIX_HEIGHT))

#define block size
BLOCK = 10

#define FPS 
FPS = pygame.time.Clock()
FPS.tick(10)

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

        #initial position of snake block is in center of screen 
        self.posx = int(PIX_HEIGHT/2)
        self.posy = int(PIX_WIDTH/2)

        #define the initial snake block 
        self.rect = pygame.Rect(self.posx,self.posy,BLOCK,BLOCK)

        #draw the initial snake block
        pygame.draw.rect(DISPLAYSURF, WHITE, self)

        #spawn the initial apple apple
        spawn_apple(self.posx, self.posy)
        
    def pos(self):
        #draw the new snake head 
        self.rect = pygame.Rect(self.posx,self.posy,BLOCK,BLOCK)

        #draw the initial snake block
        pygame.draw.rect(DISPLAYSURF, WHITE, self)
    
    def update(self):
        self.pos()

#spawn an apple at a random location 
def spawn_apple(posx, posy): 
    #creat a rectangle 10x10 pixels
    rect = pygame.Rect(0, 0, BLOCK, BLOCK)
    
    #pick a random location in the window
    surf_size = DISPLAYSURF.get_size()

    #exclude all points within a 10 block radius of the snake
    appl_x = rand.randint(BLOCK*2,(surf_size[0]-(BLOCK*2)))
    appl_y = rand.randint(BLOCK*2,(surf_size[1]-(BLOCK*2)))
    rect.center = (appl_x, appl_y)
    
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
        snake.posx += -BLOCK
        
    elif pressed_keys[K_RIGHT]:
        snake.posx += BLOCK

    elif pressed_keys[K_UP]:
        snake.posy += -BLOCK
        
    elif pressed_keys[K_DOWN]:
        snake.posy += BLOCK

def drawGrid():
    for x in range(0, PIX_WIDTH, BLOCK):
        for y in range(0, PIX_HEIGHT, BLOCK):
            rect = pygame.Rect(x, y, BLOCK, BLOCK)
            pygame.draw.rect(DISPLAYSURF, WHITE, rect, 1)
        
#Initialize snake
snake = Snake()
drawGrid()
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
    
    #check if snake ate the apple
    
    time.sleep(0.05)
    