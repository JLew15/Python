import pygame as pg
import random as r
import math
from os import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = (HEIGHT - (HEIGHT*.05))
        self.speedX = 0

    def update(self):
        self.rect.x += self.speedX

class Mob(pg.sprite.Sprite):
    def __init__(self):
        super(Mob, self).__init__()
        self.image = pg.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.top = 0
        self.speedY = 0

    def update(self):
        self.rect.y += self.speedY


# Game Constants
#################################
HEIGHT = 600
WIDTH = 300
FPS = 60
TITLE = "Shoot Em Up"

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
TURQUOISE = (0, 255, 255)
SKYBLUE = (123, 255, 255)
PASTELGREEN = (123, 255, 123)
#################################

# Init pygame and create window
#################################
pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(TITLE)
clock = pg.time.Clock()
#################################

# Load images
#################################

#################################

# Sprite Groups
#################################
allSprites = pg.sprite.Group()
playerGroup = pg.sprite.Group()
mobGroup = pg.sprite.Group()
#################################

# Create Game Obj
#################################
player1 = Player()
mob1 = Mob()
#################################

# Add Obj to Sprite Groups
#################################
player1.add(playerGroup)
mob1.add(mobGroup)


for sprite in playerGroup:
    sprite.add(allSprites)
for sprite in mobGroup:
    sprite.add(allSprites)
#################################

# Game loop
#################################
running = True

while running:

    # Timing
    #######
    clock.tick(FPS)
    #######

    # Input
    #######
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if event.type == pg.QUIT:
            running = False
    #######

    # Updates
    #######
    allSprites.update()
    #######

    # Render
    #######
    screen.fill(BLACK)
    allSprites.draw(screen)

    pg.display.flip()
    #######

pg.quit()
#################################
