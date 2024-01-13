import pygame

class Cooldown:
    def __init__( self ):
        self.run = False
        self.end = 0
    
    def start( self, time ):
        self.end = pygame.time.get_ticks() + time
        self.run = True
    
    def stop( self ):
        self.run = False
        self.end = 0

    def update( self ):
        if self.run:
            if pygame.time.get_ticks() >= self.end:
                self.stop()