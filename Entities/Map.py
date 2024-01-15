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

    def getMapGridCordsOnPosition( self, pos ):
        return [ int ( pos[ 0 ] - self.offsetX ) // self.tileSize, int ( pos[ 1 ] - self.offsetY ) // self.tileSize ]
    
    def getTileNumberOnCords( self, cords ):
        return cords[ 1 ] * self.map.size[ 0 ] + cords[ 0 ]

    def getNeighborsTilePos( self, entity ):
        center = self.getMapGridCordsOnPosition( entity.pos )
        tiles = lambda: None
        tiles.center = self.getTileNumberOnCords( [ center[ 0 ], center[ 1 ] ] )
        tiles.top = self.getTileNumberOnCords( [ center[ 0 ], center[ 1 ] - 1 ] )
        tiles.topLeft = self.getTileNumberOnCords( [ center[ 0 ] - 1, center[ 1 ] - 1 ] )
        tiles.topRight = self.getTileNumberOnCords( [ center[ 0 ] + 1, center[ 1 ] - 1 ] )
        tiles.bottom = self.getTileNumberOnCords( [ center[ 0 ], center[ 1 ] + 1 ] )
        tiles.bottomLeft = self.getTileNumberOnCords( [ center[ 0 ] - 1, center[ 1 ] + 1 ] )
        tiles.bottomRight = self.getTileNumberOnCords( [ center[ 0 ] + 1, center[ 1 ] + 1 ] )
        tiles.left = self.getTileNumberOnCords( [ center[ 0 ] - 1, center[ 1 ] ] )
        tiles.right = self.getTileNumberOnCords( [ center[ 0 ] + 1, center[ 1 ] ] )

        return tiles

    def getNewPosIfCollideWithNeighbors( self, entity ):
        tiles = self.getNeighborsTilePos( entity )

        pos = entity.pos

        if self.circleCollision( tiles.top, entity ):
            bound = self.getTileBound( tiles.top )
            pos[ 1 ] = bound.bottom + entity.radius

        if self.circleCollision( tiles.bottom, entity ):
            bound = self.getTileBound( tiles.bottom )
            pos[ 1 ] = bound.top - entity.radius

        if self.circleCollision( tiles.left, entity ):
            bound = self.getTileBound( tiles.left )
            pos[ 0 ] = bound.right + entity.radius

        if self.circleCollision( tiles.right, entity ):
            bound = self.getTileBound( tiles.right )
            pos[ 0 ] = bound.left - entity.radius

        if self.circleCollision( tiles.topLeft, entity ):
            bound = self.getTileBound( tiles.topLeft )
            pos = [ bound.right + entity.radius, bound.bottom + entity.radius ]

        if self.circleCollision( tiles.topRight, entity ):
            bound = self.getTileBound( tiles.topRight )
            pos = [ bound.left - entity.radius, bound.bottom + entity.radius ]

        if self.circleCollision( tiles.bottomLeft, entity ):
            bound = self.getTileBound( tiles.bottomLeft )
            pos = [ bound.right + entity.radius, bound.top - entity.radius ]

        if self.circleCollision( tiles.bottomRight, entity ):
            bound = self.getTileBound( tiles.bottomRight )
            pos = [ bound.left - entity.radius, bound.top - entity.radius ]

        return pos

    def getPlayerStart( self ):
        return self.getEntityStart( self.map.player[ 0 ], self.map.player[ 1 ] )

    def getEntityStart( self, x, y ):
        return [
            self.offsetX + x * self.tileSize + self.tileSize / 2,
            self.offsetY + y * self.tileSize + self.tileSize / 2
        ]
    
    def circleCollision( self, index, entity ) -> bool:

        tile = self.map.tiles[ index ]

        if not tile:
            tileLeft = self.offsetX + index % self.map.size[ 0 ] * self.tileSize
            tileTop = self.offsetY + index // self.map.size[ 0 ] * self.tileSize

            if App.Collision.circleToRect( entity.pos[ 0 ], entity.pos[ 1 ], entity.radius, tileLeft, tileTop, self.tileSize, self.tileSize ):
                return True
        
        return False

    def getTileBound( self, index ):
        bound = lambda: None
        bound.left = self.offsetX + index % self.map.size[ 0 ] * self.tileSize
        bound.top = self.offsetY + index // self.map.size[ 0 ] * self.tileSize
        bound.right = bound.left + self.tileSize
        bound.bottom = bound.top + self.tileSize
        return bound