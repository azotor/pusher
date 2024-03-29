import pygame, Entities, App

class Player( Entities.Entity ):
    def __init__( self ):
        super().__init__()
        self.speed = 30
        self.radius = 10
        self.pos = pygame.math.Vector2( 0, 0 )
        self.direction = pygame.math.Vector2( 0, 0 )
    
    def update( self ):

        dt = App.Config.FPS / 1000
        ds = self.speed * dt

        if App.controls.left:
            self.direction[ 0 ] = -1
        elif App.controls.right:
            self.direction[ 0 ] = 1
        else:
            self.direction[ 0 ] = 0

        if App.controls.up:
            self.direction[ 1 ] = -1
        elif App.controls.down:
            self.direction[ 1 ] = 1
        else:
            self.direction[ 1 ] = 0

        self.pos += self.normalizeDirection() * ds

    def render( self ):
        surf = pygame.display.get_surface()
        pygame.draw.circle( surf, App.Config.COLOR_GREEN, self.pos, self.radius )