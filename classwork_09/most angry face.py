import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((100, 100, 100))

def DrawAngry(x0, y0, size):
    circle(screen, (199, 199, 0), (x0, y0), size)
    rect(screen, (0, 0, 0), (x0 - size * 0.5, y0 + size * 0.5, size, size * 0.2))
    circle(screen, (240, 0, 0), (x0 - size * 0.4, y0 - size * 0.25), size * 0.2)
    circle(screen, (0, 0, 0), (x0 - size * 0.4, y0 - size * 0.26), size * 0.09)
    circle(screen, (240, 0, 0), (x0 + size * 0.4, y0 - size * 0.3), size * 0.15)
    circle(screen, (0, 0, 0), (x0 + size * 0.4, y0 - size * 0.3), size * 0.07)

    line(screen, (0, 0, 0), (x0 - size * 0.2, y0 - size * 0.5), (x0 - size * 0.75, y0 - size * 0.7), int(size * 0.15))
    line(screen, (0, 0, 0), (x0 + size * 0.1, y0 - size * 0.4), (x0 + size * 0.65, y0 - size * 0.6), int(size * 0.15))


DrawAngry(200, 200, 150)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()