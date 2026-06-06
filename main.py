import pygame
import sys

pygame.init()

# settig up a display window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("idlezone")  # name of display

White = (255, 255, 255)  # defining the colors using the RGB codes
Blue = (0, 0, 255)
Black = (0, 0, 0)

# Creating the Button
button = pygame.Rect(300, 250, 200, 50)  # (x, y, width, height)

font = pygame.font.Font(None, 36)  # None is the default font, 36 is fonz size
text_surface = font.render("WAKE UP", True, Black)

current_screen = "main"  # main  screen that is on

running = True
while running:
    for event in pygame.event.get():  #  This is the main loop so all the events can operate
        
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Checks if a mouse button has been clicked
            mouse_x, mouse_y = event.pos  # event.pos here calls the mouse position!!!
            if button.collidepoint(event.pos):
                current_screen = "game"    ###Here we've switched to the game screen
                print ("Start Button clicked :D")

        if current_screen == "main":
            screen.fill(Black)
            pygame.draw.rect(screen, White, button)
            screen.blit(text_surface, (344, 263))

        elif current_screen == "game":
            screen.fill(Blue)

    pygame.display.flip() # Update the display to see the changes

pygame.quit()
sys.exit()
 
