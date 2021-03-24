from pygame import *
import pygame as pg

WIDTH = 500
HEIGHT = 500
FPS = 30
title = "PINBALL"

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)


clock = pg.time.Clock()
running = True


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.image = Surface((25, 25), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, (255, 255, 255), (12.5, 12.5), 12.5)
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedX = 5
        self.speedY = -4

    def update(self):
        self.rect.centerx = self.rect.centerx + self.speedX
        self.rect.centery = self.rect.centery + self.speedY
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.speedX = self.speedX*-1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speedY = self.speedY*-1


class Kicker(pg.sprite.Sprite):
    def __init__(self):
        super(Kicker, self).__init__()
        self.image = Surface((100, 15))
        self.image.fill((255, 100, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 1.25)


ball = Ball()
allSprites = pg.sprite.Group()
allSprites.add(ball)
kicker = Kicker()
allSprites.add(kicker)

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    allSprites.update()
    screen.fill((0, 123, 255))
    allSprites.draw(screen)
    pg.display.flip()
