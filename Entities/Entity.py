import pygame

class Entity:
    def __init__( self ):
        self.pos = pygame.math.Vector2( 0, 0 )
    
    def setPos( self, pos ):
        self.pos = pos
    
    def update( self ):
        pass

    def render( self ):
        pass