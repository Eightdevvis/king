import pygame
import sys
import game

#Button Class creatioooomnnn

class Button():
    
    def __init__(self, image, x, y, scale):
        width = image.get_width()
        height = image.get_height() ##gettign height and width of the image 
        self.image = pygame.transform.scale(image, (int(scale * width), int (scale * height))) #scaling the image
        self.rect = self.image.get_rect() # creates a rectangle of the same size and all of the image
        self.rect.center = (x,y) #position it at x y (the center of the img is the pos)
        self.clicked = False

    def draw(self, surface): # I'm passing surface here too so that the buttons can be on any screen size I want (important for the calender for example)
        surface.blit(self.image, self.rect) #instead of writing screen.blit(...) we replace screen with surface (since we dont use our curretn display name as default here)
        ##-> to visualize: when we call a button named bbb -> bbb.draw(calender_screen) to make the button bbb adaptable ob the calender display<.
    
