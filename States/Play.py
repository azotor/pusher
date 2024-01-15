import States, Entities, Levels

class Play( States.State ):
    
    def __init__( self ):
        super().__init__()
    
    def enter( self ):
        self.currentLevel = 0
        self.map = Entities.Map( Levels.levels[ self.currentLevel ] )
        self.player = Entities.Player()
        self.player.pos = self.map.getPlayerStart()

    def update( self, change ):
        self.player.update()

        self.player.pos = self.map.getNewPosIfCollideWithNeighbors( self.player )

    def render( self ):
        self.map.render()
        self.player.render()