import pygame as pg
import random as r
import math
from os import *

# Code written by Jaiden Lewis
# Artwork Credit Kenney.nl or www.kenney.nl

class Projectile(pg.sprite.Sprite):
    def __init__(self, x, y):
        super(Projectile, self).__init__()
        # self.image = pg.Surface((5, 5))
        # self.image.fill(WHITE)
        self.image = bulletImg
        self.image = pg.transform.scale(bulletImg, (5, 10))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y-1
        self.speedY = -5
    def update(self):
        self.rect.y += self.speedY
        if self.rect.bottom < 0:
            self.kill()


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # self.image = pg.Surface((50, 40))
        # self.image.fill(GREEN)
        self.image = playerImg
        self.image = pg.transform.scale(playerImg, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = (WIDTH/2)
        self.rect.bottom = (HEIGHT - (HEIGHT*.05))
        self.speedX = 0

    def update(self):
        self.speedX = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.speedX = -3
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.speedX = 3
        self.rect.x += self.speedX
    def shoot(self):
        bullet = Projectile(self.rect.centerx, self.rect.top)
        projectileGroup.add(bullet)
        allSprites.add(bullet)

class Mob(pg.sprite.Sprite):
    def __init__(self):
        super(Mob, self).__init__()
        # self.image = pg.Surface((25, 25))
        # self.image.fill(RED)
        self.image = mobImg
        self.image = pg.transform.scale(mobImg, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.centerx = r.randint(13, WIDTH-13)
        self.rect.top = 0
        self.speedY = r.randint(1, 10)
        self.speedX = r.randint(-3, 3)

    def update(self):
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.centerx = r.randint(13, WIDTH - 13)
            self.speedY = r.randint(1, 10)
            self.speedX = r.randint(-3, 3)
        self.rect.x += self.speedX
        self.rect.y += self.speedY
    def spawnNPC(self):
        npc = Mob()
        mobGroup.add(npc)
        allSprites.add(npc)


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

# Init Folders
#################################
gameFolder = path.dirname(__file__)
imgs = path.join(gameFolder, "img")
saveData = path.join(gameFolder, "data")
aud = path.join(gameFolder, "media")
playerimgs = path.join(imgs, "player")
mobimgs = path.join(imgs, "mob")
bgimg = path.join(imgs, "bg")
print(imgs)
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
bg = pg.image.load(bgimg + "/bg.png")
bgRect = bg.get_rect()
playerImg = pg.image.load(playerimgs + "/shooter.png")
playerRect = playerImg.get_rect()
bulletImg = pg.image.load(playerimgs + "/shot.png")
bulletRect = bulletImg.get_rect()
mobImg = pg.image.load(mobimgs + "/shooting.png")
mobRect = mobImg.get_rect()
#################################

# Sprite Groups
#################################
allSprites = pg.sprite.Group()
playerGroup = pg.sprite.Group()
mobGroup = pg.sprite.Group()
projectileGroup = pg.sprite.Group()
#################################

# Create Game Obj
#################################
player1 = Player()
mob1 = Mob()
for i in range(10):
    mob1.spawnNPC()
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
            if event.key == pg.K_SPACE:
                player1.shoot()
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
    screen.blit(bg, bgRect)
    allSprites.draw(screen)

    pg.display.flip()
    #######

pg.quit()
#################################
