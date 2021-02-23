import random
import pygame

HEIGHT = 200
WIDTH = 200
FPS = 30
title = "TEMPLATE"

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(title)

clock = pygame.time.Clock()
