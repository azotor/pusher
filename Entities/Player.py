import pygame, Entities, App

class Player( Entities.Entity ):
    def __init__( self ):
        super().__init__()
        self.speed = 30
        self.radius = 10
        self.pos = pygame.math.Vector2( 100, 100 )
    
    def update( self ):
        dt = App.Config.FPS / 1000
        ds = self.speed * dt

        if App.controls.up:
            self.pos[ 1 ] -= ds
        elif App.controls.down:
            self.pos[ 1 ] += ds

        if App.controls.left:
            self.pos[ 0 ] -= ds
        elif App.controls.right:
            self.pos[ 0 ] += ds

    def render( self ):
        self.surf = pygame.display.get_surface()
        pygame.draw.circle( self.surf, App.Config.COLOR_GREEN, self.pos, self.radius )