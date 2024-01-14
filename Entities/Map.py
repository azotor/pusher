import pygame, App, math

class Map:

    def __init__( self, map ):
        self.map = map
        self.tileSize = 50

        self.offsetX = ( App.Config.WINDOW_WIDTH - self.map.size[ 0 ] * self.tileSize ) / 2
        self.offsetY = ( App.Config.WINDOW_HEIGHT - self.map.size[ 1 ] * self.tileSize ) / 2

    def update( self ):
        pass

    def render( self ):
        self.surf = pygame.display.get_surface()

        for index, tile in enumerate( self.map.tiles ):
            rect = ( self.offsetX + index % self.map.size[ 0 ] * self.tileSize, self.offsetY + index // self.map.size[ 0 ] * self.tileSize, self.tileSize, self.tileSize )
            pygame.draw.rect( self.surf, App.Config.COLOR_WHITE if tile else App.Config.COLOR_BLACK, rect )
            pygame.draw.rect( self.surf, App.Config.COLOR_LIGHT if tile else App.Config.COLOR_DARKER, rect, 1 )
    
    def circleCollision( self, entity ) -> int:

        for index, tile in enumerate( self.map.tiles ):

            if not tile:
                tileLeft = self.offsetX + index % self.map.size[ 0 ] * self.tileSize
                tileTop = self.offsetY + index // self.map.size[ 0 ] * self.tileSize

                if App.Collision.circleToRect( entity.pos[ 0 ], entity.pos[ 1 ], entity.radius, tileLeft, tileTop, self.tileSize, self.tileSize ):
                    return index
        
        return -1
    
    def getTileBound( self, index ):
        bound = lambda: None
        bound.left = self.offsetX + index % self.map.size[ 0 ] * self.tileSize
        bound.top = self.offsetY + index // self.map.size[ 0 ] * self.tileSize
        bound.right = bound.left + self.tileSize
        bound.bottom = bound.top + self.tileSize
        # bound.width = self.tileSize
        # bound.height = self.tileSize
        # bound.centerX = bound.left + self.tileSize / 2
        # bound.centerY = bound.top + self.tileSize / 2
        # bound.radius = math.sqrt( self.tileSize ** 2 + self.tileSize ** 2 ) / 2
        return bound

    def getPlayerStart( self ):
        return self.getEntityStart( self.map.player[ 0 ], self.map.player[ 1 ] )

    def getEntityStart( self, x, y ):
        return [
            self.offsetX + x * self.tileSize + self.tileSize / 2,
            self.offsetY + y * self.tileSize + self.tileSize / 2
        ]