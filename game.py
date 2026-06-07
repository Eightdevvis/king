import pygame
import sys

def run(screen, White, Blue, Black, width, height):  # use these def from main.py

     background = pygame.image.load("idlesketch.png")
     background = pygame.transform.scale(background, (width, height))

     cursor_surface = pygame.image.load("idlemouse.png").convert_alpha()
     cursor = pygame.cursors.Cursor((0, 0), cursor_surface)
     pygame.mouse.set_cursor(cursor)

     running = True
     while running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            screen.blit(background, (0, 0))
            pygame.display.flip() # constant update of the display
