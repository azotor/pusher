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
        if self.map.circleCollision( self.player ):
            print( "kolizja" )

    def render( self ):
        self.map.render()
        self.player.render()