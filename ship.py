#Pygame lets us treat all game elements like rectangles (rects) even if they're not exactly shaped
# The class takes two paremeters, the self reference and a reference to the current instance of AlienInvasion class


import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_game):
        """Initialize the ship and set starting position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() #We access the screen's rect attribute using the get_rect() method

        #load the ship image and get its rect

        self.image = pygame.image.load('images/ship.bmp') #Load the image and give the location of the image
        self.rect = self.image.get_rect() #when the image is loaded we call get_rect() to access the ship's surface rect attribute

        #start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom #We make the value of rect.midbottom match the midbottom attribute of the screen's rect

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #movement flag
        self.moving_right = False #When false the ship will be motionless
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""

        # Update the ship's x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right: #Limiting the range
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self): #This method draws the image to the screen at the position specified by self.rect
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect) 

    def center_ship(self):
        """ Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

