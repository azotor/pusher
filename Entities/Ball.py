import pygame, math, Entities, App

class Ball( Entities.Entity ):
    def __init__( self ):
        super().__init__()
        self.speed = 30
        self.radius = 6
        self.pos = pygame.math.Vector2( 0, 0 )
        self.direction = pygame.math.Vector2( 0, 0 )
        self.lock = False
        self.inHoll = False
    
    def convertAngleToDirection( self, angle ):
        self.direction[ 0 ] = math.cos( angle ) * self.speed
        self.direction[ 1 ] = math.sin( angle ) * self.speed
    
    def update( self ):
        self.pos[ 0 ] += self.direction[ 0 ] * ( App.Config.FPS / 1000 )
        self.pos[ 1 ] += self.direction[ 1 ] * ( App.Config.FPS / 1000 )

    def render( self ):
        surf = pygame.display.get_surface()

        pygame.draw.circle( surf, App.Config.COLOR_PURPLE, self.pos, self.radius )