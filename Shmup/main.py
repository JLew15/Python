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
        self.rect.bottom = y - 1
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
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = (HEIGHT - (HEIGHT * .05))
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
        self.imageO = mobImg
        self.imageO = pg.transform.scale(mobImg, (25, 25))
        self.image = self.imageO.copy()
        self.rect = self.image.get_rect()
        self.rect.centerx = r.randint(13, WIDTH - 13)
        self.rect.top = 0
        self.speedY = r.randint(1, 10)
        self.speedX = r.randint(-3, 3)
        self.last_update = pg.time.get_ticks()
        self.rot = 0
        self.rotSpeed = r.randint(-8, 8)

    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 60:
            self.last_update = now
            self.rot = (self.rot + self.rotSpeed) % 360
            newImage = pg.transform.rotate(self.imageO, self.rot)
            oldCenter = self.rect.center
            self.image = newImage
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter

    def update(self):
        self.rotate()
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
playerLives = 5
playerScore = 0
fontName = pg.font.match_font("arial")

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

def drawText(surf, text, size, x, y):
    font = pg.font.Font(fontName, size)
    txtSurface = font.render(text, True, WHITE)
    textRect = txtSurface.get_rect()
    textRect.midtop = (x, y)
    surf.blit(txtSurface, textRect)


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

    hits = pg.sprite.spritecollide(player1, mobGroup, True)
    if hits:
        print("Player hit")
        mob1.spawnNPC()
        playerLives -= 1
        playerScore -= 10
        if playerLives <= 0:
            player1.kill()
    hits = pg.sprite.groupcollide(projectileGroup, mobGroup, True, True)
    for hit in hits:
        mob1.spawnNPC()
        playerScore += 5
        if playerScore % 100 == 0:
            playerLives += 1
            print("LIFE GAINED")

    #######

    # Render
    #######
    screen.fill(BLACK)
    screen.blit(bg, bgRect)
    allSprites.draw(screen)
    drawText(screen,"Score: " + str(playerScore), 18, WIDTH/2, 10)

    pg.display.flip()
    #######

pg.quit()
#################################
