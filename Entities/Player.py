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
        self.surf = pygame.display.get_surface()
        pygame.draw.circle( self.surf, App.Config.COLOR_GREEN, self.pos, self.radius )

    def colissionPosConvert( self, bound ):

        if self.direction[ 1 ] == 0:
            if self.direction[ 0 ] == 1:
                self.pos[ 0 ] = bound.left - self.radius
            elif self.direction[ 0 ] == -1:
                self.pos[ 0 ] = bound.right + self.radius
        else:
            pass
        
        if self.direction[ 0 ] == 0:
            if self.direction[ 1 ] == 1:
                self.pos[ 1 ] = bound.top - self.radius
            elif self.direction[ 1 ] == -1:
                self.pos[ 1 ] = bound.bottom + self.radius
        else:
            pass

        # skosy?