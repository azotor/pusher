import pygame, Entities, App

class Holl( Entities.Entity ):
    def __init__( self ):
        super().__init__()
        self.radius = 8
        self.pos = pygame.math.Vector2( 0, 0 )
    
    def update( self ):
        pass

    def render( self ):
        surf = pygame.display.get_surface()

        pygame.draw.circle( surf, App.Config.COLOR_PURPLE, self.pos, self.radius, 1 )
        pygame.draw.circle( surf, App.Config.COLOR_PURPLE, self.pos, self.radius - 2, 1 )