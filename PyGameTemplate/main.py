import random
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speedX = 5
        self.speedY = 0

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.top = HEIGHT
            self.rect.x = WIDTH/2
            self.speedX = 0
            self.speedY = -5
        if self.rect.right < 0:
            self.rect.bottom = 0
            self.rect.x = WIDTH/2
            self.speedX = 0
            self.speedY = 5
        if self.rect.top > HEIGHT:
            self.rect.left = 0
            self.rect.y = HEIGHT/2
            self.speedX = 5
            self.speedY = 0
        if self.rect.bottom < 0:
            self.rect.left = WIDTH
            self.rect.y = HEIGHT/2
            self.speedX = -5
            self.speedY = 0
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

allSprites.add(player)

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    allSprites.update()
    screen.fill(GREEN)
    allSprites.draw(screen)
    pygame.display.flip()
