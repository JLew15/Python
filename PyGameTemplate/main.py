import math
import random
import pygame
import os


gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder, "img")
audFolder = os.path.join(gameFolder, "aud")
mouseHeld = False

class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedX = 5
        self.speedY = 6
        self.angle = 0
        self.doCircle = False

    def update(self):
        if self.rect.right >= WIDTH - 1 or self.rect.left <= 1:
            self.speedX = -self.speedX
            if self.speedX < 0:
                self.speedX -= 1
            else:
                self.speedX += 1
        if self.rect.bottom >= HEIGHT - 1 or self.rect.top <= 1:
            self.speedY = -self.speedY
            if self.speedY < 0:
                self.speedY -= 1
            else:
                self.speedY += 1
        self.rect.x += self.speedX
        self.rect.y += self.speedY


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = playerImage
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedX = 0
        self.speedY = 0

    def update(self):
        if mouseHeld:
            self.rect.center = (mouseX, mouseY)


def spawnNewNPC(x, y):
    newNPC = NPC()
    newNPC.rect.center = (x,y)
    newNPC.speedX = random.randint(-10, 10)
    newNPC.speedY = random.randint(-10, 10)
    allSprites.add(newNPC)
    mobGroup.add(newNPC)



HEIGHT = 350
WIDTH = 350
FPS = 30
title = "TEMPLATE"

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

pygame.init()
pygame.mixer.init()



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(title)

playerImage = pygame.image.load(os.path.join(imgFolder, "sprites/player/bubblegum.png")).convert()

clock = pygame.time.Clock()
running = True
allSprites = pygame.sprite.Group()
playersGroup = pygame.sprite.Group()
mobGroup = pygame.sprite.Group()

player = Player()
npc = NPC()

allSprites.add(player)
allSprites.add(npc)
playersGroup.add(player)
mobGroup.add(npc)

while running:
    clock.tick(FPS)
    mouseX, mouseY = pygame.mouse.get_pos()
    # print(mouseX)
    # print(mouseY)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pressed(3)
            if x[0] and player.rect.collidepoint(pygame.mouse.get_pos()):
                mouseHeld = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouseHeld = False
            spawnNewNPC(mouseX, mouseY)

        if event.type == pygame.QUIT:
            running = False

    allSprites.update()
    screen.fill(GREEN)
    allSprites.draw(screen)
    pygame.display.flip()
