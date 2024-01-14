import pygame

class Entity:
    def __init__( self ):
        self.pos = None
        self.direction = pygame.math.Vector2( 0, 0 )
    
    def setPos( self, pos ):
        self.pos = pos
    
    def update( self ):
        pass

    def render( self ):
        pass

    def normalizeDirection( self ):
        return self.direction.normalize() if self.direction[ 0 ] != 0 or self.direction[ 1 ] != 0 else pygame.math.Vector2( 0, 0 )