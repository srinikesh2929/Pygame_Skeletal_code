import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))

running = 1

while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0
    else:
      print (event)

  screen.fill((120, 120, 120))
  pygame.display.flip()

pygame.quit()
