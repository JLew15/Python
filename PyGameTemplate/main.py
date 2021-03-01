import math
import random
import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speedX = 5
        self.speedY = 6
        self.angle = 0
        self.doCircle = False

    def update(self):
        if self.rect.right >= WIDTH-1 or self.rect.left <= 1:
            self.speedX = -self.speedX
            if self.speedX < 0:
                self.speedX -= 1
            else:
                self.speedX += 1
        if self.rect.bottom >= HEIGHT-1 or self.rect.top <=1:
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
        self.image = pygame.Surface((50, 50))
        self.image.fill(SKYBLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speedX = 0
        self.speedY = 0

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY


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
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speedX = -5
            if event.key == pygame.K_RIGHT:
                player.speedX = 5
            if event.key == pygame.K_UP:
                player.speedY = -5
            if event.key == pygame.K_DOWN:
                player.speedY = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.speedX = -0
            if event.key == pygame.K_RIGHT:
                player.speedX = 0
            if event.key == pygame.K_UP:
                player.speedY = -0
            if event.key == pygame.K_DOWN:
                player.speedY = 0

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         player.rect.x -= 50
        #     if event.key == pygame.K_RIGHT:
        #         player.rect.x += 50
        #     if event.key == pygame.K_UP:
        #         player.rect.y -= 50
        #     if event.key == pygame.K_DOWN:
        #         player.rect.y += 50
        if event.type == pygame.QUIT:
            running = False

    allSprites.update()
    screen.fill(GREEN)
    allSprites.draw(screen)
    pygame.display.flip()
