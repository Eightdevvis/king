import pygame
import sys
from storygame import Button

#calender
calender = pygame.image.load("Calender.png")
calender = pygame.transform.scale(calender, (850, 500))
calenderview = pygame.display.set_mode ((600,300))
pygame.display.set_caption("CalView")
calender_button = Button(calender, 700, 180, 1)

def run(screen, White, Blue, Black, width, height, current_screen):  # use these def from main.py

     background = pygame.image.load("idlesketch.png")
     background = pygame.transform.scale(background, (width, height))

     # Cursor
     cursor_surface = pygame.image.load("idlemouse.png").convert_alpha()  #Cursor shape
     cursor = pygame.cursors.Cursor((0, 0), cursor_surface)
     pygame.mouse.set_cursor(cursor)  # changing the actual cursor to my own


     
     running = True
     while running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if calender_button.rect.collidepoint(event.pos):
                    current_screen = "CalView"
                    print ("Calender Opened!")
                    ## open calender
            

            screen.blit(background, (0, 0)) #has to come before calender button since it would hide it otherwirse lmfao
            calender_button.draw(screen) # draw the damn button on the screen rn not on the calview, since calview is a whole diff window pop up after clicking the button


            
            pygame.display.flip() # constant update of the display
