import pygame, App

class Events:

    def __init__( self ):
        self.running = True

    def update( self ):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        App.controls.up = True if keys[ pygame.K_UP ] else False
        App.controls.right = True if keys[ pygame.K_RIGHT ] else False
        App.controls.down = True if keys[ pygame.K_DOWN ] else False
        App.controls.left = True if keys[ pygame.K_LEFT ] else False
        App.controls.select = True if keys[ pygame.K_RETURN ] else False
        App.controls.action = True if keys[ pygame.K_SPACE ] else False
        App.controls.reset = True if keys[ pygame.K_r ] else False
        App.controls.escape = True if keys[ pygame.K_ESCAPE ] else False

events = Events()