import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
ELEMENTCOLOUR = (100, 100, 100)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Ping Pong Game!')
 
# The main function that controls the game
def main () :
  looping = True
  
  # The main game loop
  while looping :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
    
    # Processing
    # This section will be built out later
 
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.draw.line(WINDOW, ELEMENTCOLOUR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), 2)
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()
